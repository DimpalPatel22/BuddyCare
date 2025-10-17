let slides = document.querySelectorAll('.slide'); // get all slides
let current = 0;                                  // current slide index

setInterval(() => {                               // repeat every 5 seconds
    slides[current].classList.remove('active');  // hide current slide
    current = (current + 1) % slides.length;     // move to next slide, loop to first
    slides[current].classList.add('active');     // show next slide
}, 5000);
