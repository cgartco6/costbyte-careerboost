document.addEventListener("DOMContentLoaded", () => {

    const menuBtn = document.querySelector(".hamburger");
    const nav = document.querySelector(".nav-menu");

    menuBtn.addEventListener("click", () => {
        nav.classList.toggle("nav-active");
        menuBtn.classList.toggle("open");
    });

    document.querySelectorAll("[data-route]").forEach(link => {
        link.addEventListener("click", e => {
            e.preventDefault();
            loadPage(e.target.dataset.route);
            nav.classList.remove("nav-active");
            menuBtn.classList.remove("open");
        });
    });
});

function loadPage(page) {
    fetch(`pages/${page}.html`)
        .then(res => res.text())
        .then(html => {
            document.querySelector("#main").innerHTML = html;
        });
}
