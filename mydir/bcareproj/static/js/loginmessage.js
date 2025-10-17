document.addEventListener("DOMContentLoaded", function() {
    const marquee = document.querySelector('.marquee-content');
    if (!marquee) return;

    let count = 0;
    const total = 4; // slide 3 times
    const slide = () => {
        marquee.style.transition = 'transform 8s linear';
        marquee.style.transform = 'translateX(-100%)';

        setTimeout(() => {
            count++;
            if (count < total) {
                marquee.style.transition = 'none';
                marquee.style.transform = 'translateX(100%)';
                setTimeout(slide, 50); // small delay before next slide
            } else {
                // remove after 3 slides
                marquee.parentElement.style.display = 'none';
            }
        }, 6000); // match transition duration
    }

    slide();
});

