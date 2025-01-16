import urllib.request
import cv2
import mediapipe as mp
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Label, StringVar, OptionMenu, Frame, Button, Entry, messagebox
import sqlite3
import os
from datetime import datetime
import threading
import queue

class HandDetector:
    def __init__(self):
        # Inicializar la base de datos
        self.init_database()

        # Configuración de la ventana principal
        self.root = tk.Tk()
        self.root.title("Contador de Dedos - Webcam/IP Cam")

        # Frame para selección de cámara y URL
        self.camera_frame = Frame(self.root)
        self.camera_frame.pack(pady=5)

        # Menú para seleccionar cámara y entrada de URL para IP Cam
        self.available_cameras = ["Webcam", "IP Cam"]
        self.selected_camera = StringVar(self.root)
        self.selected_camera.set(self.available_cameras[0])

        Label(self.camera_frame, text="Seleccionar cámara:").pack(side=tk.LEFT, padx=5)
        self.camera_menu = OptionMenu(self.camera_frame, self.selected_camera, *self.available_cameras)
        self.camera_menu.pack(side=tk.LEFT, padx=5)

        Label(self.camera_frame, text="URL de IP Cam:").pack(side=tk.LEFT, padx=5)
        self.ip_url_entry = Entry(self.camera_frame, width=30)
        self.ip_url_entry.insert(0, "http://10.65.200.219:8080/video")  # URL de ejemplo
        self.ip_url_entry.pack(side=tk.LEFT, padx=5)

        self.reconnect_button = Button(self.camera_frame, text="Reconectar", command=self.reconnect_camera)
        self.reconnect_button.pack(side=tk.LEFT, padx=5)

        # Inicializar la cámara web
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Inicializar mediapipe para detección de manos
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=2)
        self.mp_drawing = mp.solutions.drawing_utils

        # Configurar la interfaz de video
        self.label = Label(self.root)
        self.label.pack()

        # Frame para formulario de registro
        self.form_frame = Frame(self.root)
        self.form_frame.pack(pady=10)

        # Campos de entrada
        Label(self.form_frame, text="ID:").pack(side=tk.LEFT, padx=5)
        self.id_entry = Entry(self.form_frame)
        self.id_entry.pack(side=tk.LEFT, padx=5)

        Label(self.form_frame, text="Nombre:").pack(side=tk.LEFT, padx=5)
        self.name_entry = Entry(self.form_frame)
        self.name_entry.pack(side=tk.LEFT, padx=5)

        # Botones
        self.register_button = Button(self.form_frame, text="Registrar", command=self.register_user)
        self.register_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = Button(self.form_frame, text="Limpiar Registro", command=self.clear_registration)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Frame para información del usuario actual
        self.user_info_frame = Frame(self.root)
        self.user_info_frame.pack(pady=5)
        self.current_user_label = Label(self.user_info_frame, text="Usuario no registrado", font=("Arial", 12, "bold"))
        self.current_user_label.pack()

        # Labels para información de manos
        self.hand_info_frame = Frame(self.root)
        self.hand_info_frame.pack(pady=10)

        # Crear frames separados para cada mano
        self.hand1_frame = Frame(self.hand_info_frame, relief=tk.RAISED, borderwidth=1)
        self.hand1_frame.pack(side=tk.LEFT, padx=10, pady=5)
        self.hand2_frame = Frame(self.hand_info_frame, relief=tk.RAISED, borderwidth=1)
        self.hand2_frame.pack(side=tk.LEFT, padx=10, pady=5)

        # Labels para Mano 1 (derecha)
        Label(self.hand1_frame, text="Mano Derecha", font=("Arial", 12, "bold")).pack()
        self.hand1_user_label = Label(self.hand1_frame, text="Sin usuario", font=("Arial", 10))
        self.hand1_user_label.pack()
        self.hand1_fingers_label = Label(self.hand1_frame, text="Sin detectar", font=("Arial", 10))
        self.hand1_fingers_label.pack()

        # Labels para Mano 2 (izquierda)
        Label(self.hand2_frame, text="Mano Izquierda", font=("Arial", 12, "bold")).pack()
        self.hand2_user_label = Label(self.hand2_frame, text="Sin usuario", font=("Arial", 10))
        self.hand2_user_label.pack()
        self.hand2_fingers_label = Label(self.hand2_frame, text="Sin detectar", font=("Arial", 10))
        self.hand2_fingers_label.pack()

        # Variables para tracking de usuarios y manos
        self.hand1_user_id = None
        self.hand1_user_name = None
        self.hand2_user_id = None
        self.hand2_user_name = None
        self.current_user_id = None
        self.current_user_name = None

        # Cargar último usuario registrado
        self.load_last_user()

        # Cola para manejar los fotogramas de video
        self.frame_queue = queue.Queue(maxsize=5)
        self.running = False

    def init_database(self):
        """Inicializar la base de datos"""
        self.conn = sqlite3.connect('hand_detection.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            last_registered INTEGER DEFAULT 0
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS hand_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            hand_position TEXT,
            fingers_count INTEGER,
            timestamp DATETIME,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )''')

        self.conn.commit()

    def load_last_user(self):
        """Cargar el último usuario registrado"""
        try:
            self.cursor.execute('SELECT id, name FROM users WHERE last_registered = 1')
            result = self.cursor.fetchone()
            if result:
                self.current_user_id, self.current_user_name = result
                self.current_user_label.config(text=f"Usuario actual: {self.current_user_name} (ID: {self.current_user_id})")
                self.id_entry.delete(0, tk.END)
                self.id_entry.insert(0, self.current_user_id)
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, self.current_user_name)
            else:
                print("No hay usuarios registrados.")
        except sqlite3.Error as e:
            print(f"Error al cargar el último usuario: {e}")

    def register_user(self):
        """Registrar un nuevo usuario"""
        user_id = self.id_entry.get()
        user_name = self.name_entry.get()

        if user_id and user_name:
            try:
                self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
                if self.cursor.fetchone():
                    messagebox.showwarning("Advertencia", "Este ID de usuario ya está registrado.")
                    return

                # Registrar el nuevo usuario
                self.cursor.execute('INSERT INTO users (id, name) VALUES (?, ?)', (user_id, user_name))
                self.conn.commit()

                # Marcar este usuario como el último registrado
                self.cursor.execute('UPDATE users SET last_registered = 0')
                self.cursor.execute('UPDATE users SET last_registered = 1 WHERE id = ?', (user_id,))
                self.conn.commit()

                # Actualizar la interfaz de usuario
                self.current_user_id = user_id
                self.current_user_name = user_name
                self.current_user_label.config(text=f"Usuario actual: {user_name}")

                # Limpiar campos
                self.id_entry.delete(0, tk.END)
                self.name_entry.delete(0, tk.END)

                messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
            except sqlite3.Error as e:
                print(f"Error al registrar usuario: {e}")
                messagebox.showerror("Error", "No se pudo registrar el usuario.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def clear_registration(self):
        """Limpiar registro de usuario"""
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.current_user_label.config(text="Usuario no registrado")
        self.current_user_id = None
        self.current_user_name = None
        self.hand1_user_id = None
        self.hand1_user_name = None
        self.hand2_user_id = None
        self.hand2_user_name = None
        self.hand1_user_label.config(text="Sin usuario")
        self.hand2_user_label.config(text="Sin usuario")

        try:
            self.cursor.execute('UPDATE users SET last_registered = 0')
            self.conn.commit()
            messagebox.showinfo("Éxito", "Registro limpiado correctamente")
        except sqlite3.Error as e:
            print(f"Error al limpiar registro: {e}")
            messagebox.showerror("Error", "Error al limpiar el registro")

    def check_ip_camera(self, url):
        """Verificar la disponibilidad de la cámara IP"""
        try:
            response = urllib.request.urlopen(url)
            return response.status == 200
        except Exception as e:
            print(f"Error al acceder a la cámara IP: {e}")
            return False

    def reconnect_camera(self):
        """Reconectar la cámara IP"""
        if self.selected_camera.get() == "IP Cam":
            url = self.ip_url_entry.get()
            if self.check_ip_camera(url):
                self.cap.release()  # Liberar cámara anterior
                self.cap = cv2.VideoCapture(url)  # Conectar a nueva URL
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Tamaño más pequeño
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
                if not self.cap.isOpened():
                    messagebox.showerror("Error", "No se pudo conectar a la cámara IP.")
                else:
                    messagebox.showinfo("Éxito", "Conectado a la cámara IP.")
            else:
                messagebox.showerror("Error", "La URL de la cámara IP no es accesible.")
        else:
            # Reconectar la cámara web
            self.cap.release()
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "No se pudo conectar a la cámara web.")

    def contarDedos(self, hand_landmarks):
        """Contar los dedos levantados en la mano detectada"""
        dedos = []
        
        # Índices de las puntas de los dedos
        tip_ids = [4, 8, 12, 16, 20]
        
        # Pulgar
        if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 2].x:
            dedos.append(1)
        else:
            dedos.append(0)
        
        # Otros dedos
        for i in range(1, 5):
            if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
                dedos.append(1)
            else:
                dedos.append(0)
        
        return sum(dedos)

    def save_hand_record(self, hand_position, fingers_count):
        """Guardar el registro de la mano en la base de datos"""
        if self.current_user_id:
            try:
                self.cursor.execute('''
                    INSERT INTO hand_records (user_id, hand_position, fingers_count, timestamp)
                    VALUES (?, ?, ?, ?)
                ''', (self.current_user_id, hand_position, fingers_count, datetime.now()))
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Error al guardar registro: {e}")

    def process_frame(self, frame):
        """Procesar el fotograma de la cámara"""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        # Resetear estados de detección
        hand1_detected = False
        hand2_detected = False
        
        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                # Dibujar landmarks
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # Contar dedos
                dedos_detectados = self.contarDedos(hand_landmarks)
                
                # Determinar posición de la mano (derecha o izquierda)
                hand_position = "Derecha" if hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x > 0.5 else "Izquierda"
                
                # Manejar detección y actualización de cada mano
                if hand_position == "Derecha":
                    hand1_detected = True
                    if not self.hand1_user_id:  # Si la mano derecha no tiene usuario asignado
                        self.hand1_user_id = self.current_user_id
                        self.hand1_user_name = self.current_user_name
                    if self.hand1_user_id and self.hand1_user_name:
                        user_text = f"ID: {self.hand1_user_id} - {self.hand1_user_name}"
                        self.hand1_user_label.config(text=user_text)
                        self.hand1_fingers_label.config(text=f"Dedos detectados: {dedos_detectados}")
                        self.save_hand_record("Mano Derecha", dedos_detectados)
                
                elif hand_position == "Izquierda":
                    hand2_detected = True
                    if not self.hand2_user_id:  # Si la mano izquierda no tiene usuario asignado
                        self.hand2_user_id = self.current_user_id
                        self.hand2_user_name = self.current_user_name
                    if self.hand2_user_id and self.hand2_user_name:
                        user_text = f"ID: {self.hand2_user_id} - {self.hand2_user_name}"
                        self.hand2_user_label.config(text=user_text)
                        self.hand2_fingers_label.config(text=f"Dedos detectados: {dedos_detectados}")
                        self.save_hand_record("Mano Izquierda", dedos_detectados)
        
        # Actualizar labels para manos no detectadas
        if not hand1_detected:
            self.hand1_fingers_label.config(text="Sin detectar")
            if not self.hand1_user_id:
                self.hand1_user_label.config(text="Sin usuario")
        
        if not hand2_detected:
            self.hand2_fingers_label.config(text="Sin detectar")
            if not self.hand2_user_id:
                self.hand2_user_label.config(text="Sin usuario")
        
        return frame

    def start_camera(self):
        """Iniciar el bucle de captura de la cámara"""
        self.running = True
        self.update_frames()

    def update_frames(self):
        """Actualizar los fotogramas en la interfaz"""
        ret, frame = self.cap.read()
        if ret:
            frame = self.process_frame(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_image = Image.fromarray(frame)
            frame_image = frame_image.resize((320, 240), Image.LANCZOS)
            frame_image = ImageTk.PhotoImage(image=frame_image)
            self.label.config(image=frame_image)
            self.label.image = frame_image

        if self.running:
            self.root.after(10, self.update_frames)

    def stop_camera(self):
        """Detener la cámara"""
        self.running = False
        self.cap.release()
        self.hands.close()
        self.conn.close()
        self.root.quit()

if __name__ == "__main__":
    app = HandDetector()
    app.start_camera()
    app.root.protocol("WM_DELETE_WINDOW", app.stop_camera)
    app.root.mainloop()

