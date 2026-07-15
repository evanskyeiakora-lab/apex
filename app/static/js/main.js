const swiper = new Swiper(".heroSwiper", {
    loop: true,
    autoplay: {
        delay: 5000,
    },
    effect: "fade",
    speed: 1000,

    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    }
});