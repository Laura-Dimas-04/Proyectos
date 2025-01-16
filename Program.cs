namespace Prueba3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    Console.WriteLine(@"
1) Kilómetros a metros
2) Metros a kilómetros
3) Kilómetros a millas
4) Millas a Kilómetros
5) Salir
");
                    Console.WriteLine("Por favor elija de una de las 5 opciones: ");
                    int opciones = Convert.ToInt32(Console.ReadLine());

                    switch (opciones)
                    {
                        case 1:
                            Console.WriteLine("Ingrese los kilometros que desea convertir a metros: ");
                            double kilos = Convert.ToDouble(Console.ReadLine());
                            Console.WriteLine("El resultado de kilómetros a metros es = " + (kilos * 1000) + " metros");
                            break;

                        case 2:
                            Console.WriteLine("Ingrese los metros que desea convertir a kilometros");
                            double metro = Convert.ToDouble(Console.ReadLine());
                            Console.WriteLine("El resultado de metros a kilometros es =" + (metro * 1 / 1000) + "kilometros");
                            break;

                        case 3:
                            Console.WriteLine("Ingrese los kilometros que desea convertir a millas");
                            double kilo = Convert.ToDouble(Console.ReadLine());
                            Console.WriteLine("El resultado de jilometros a millas es =" + (kilo * 1.609) + "millas");
                            break;

                        case 4:
                            Console.WriteLine("Ingrese los kilometros que desea convertir a millas");
                            double millas = Convert.ToDouble(Console.ReadLine());
                            Console.WriteLine("El resultado de jilometros a millas es =" + (millas * 1.609) + "millas");
                            break;

                        case 5:
                            Console.WriteLine("Saliendo del programa...");
                            return; // Sale del programa

                        default:
                            Console.WriteLine("Opción no válida. Intente de nuevo.");
                            break;
                    }

                }
                catch (FormatException)
                {
                    Console.WriteLine("Entrada no válida. Por favor ingrese un número.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Ocurrió un error: " + ex.Message);
                }
            }
        }
    }
}


