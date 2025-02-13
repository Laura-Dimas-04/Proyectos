document.addEventListener('DOMContentLoaded', () => {
    const noBtn = document.getElementById('noBtn');
    const yesBtn = document.getElementById('yesBtn');
    const message = document.getElementById('message');
    const title = document.querySelector('.title');
    const clouds = document.querySelectorAll('.contenedor img');
    const button = document.querySelector('.button');

    function createHeart() {
        const heart = document.createElement('div');
        heart.className = 'floating-heart';
        heart.textContent = '💙';
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDuration = (Math.random() * 2 + 3) + 's';
        heart.style.fontSize = '40px';
        heart.style.color = 'blue';
        document.body.appendChild(heart);

        heart.addEventListener('animationend', () => {
            heart.remove();
        });
    }

    function startHeartAnimation() {
        for (let i = 0; i < 10; i++) {
            setTimeout(createHeart, i * 300);
        }

        setInterval(createHeart, 300);
    }

    yesBtn.addEventListener('click', () => {
        noBtn.style.display = 'none';
        yesBtn.style.display = 'none';
        message.style.display = 'block';
        button.style.display = 'block';
        startHeartAnimation();

        // Fijar posición del body y ocultar overflow
        document.body.style.position = 'fixed';
        document.body.style.overflow = 'hidden';
    });

    noBtn.addEventListener('mouseover', moveButton);

    function moveButton() {
        let x, y, isOverlapping;
        do {
            isOverlapping = false;
            x = Math.random() * (window.innerWidth - noBtn.offsetWidth);
            y = Math.random() * (window.innerHeight - noBtn.offsetHeight);

            // Check if overlapping with title
            const titleRect = title.getBoundingClientRect();
            if (x < titleRect.right && x + noBtn.offsetWidth > titleRect.left &&
                y < titleRect.bottom && y + noBtn.offsetHeight > titleRect.top) {
                isOverlapping = true;
            }

            // Check if overlapping with any cloud
            clouds.forEach(cloud => {
                const cloudRect = cloud.getBoundingClientRect();
                if (x < cloudRect.right && x + noBtn.offsetWidth > cloudRect.left &&
                    y < cloudRect.bottom && y + noBtn.offsetHeight > cloudRect.top) {
                    isOverlapping = true;
                }
            });
        } while (isOverlapping);

        // Move noBtn quickly and pass over yesBtn
        noBtn.style.transition = 'left 0.5s, top 0.5s';
        noBtn.style.zIndex = '21';
        noBtn.style.position = 'absolute';
        noBtn.style.left = `${x}px`;
        noBtn.style.top = `${y}px`;
    }
});
