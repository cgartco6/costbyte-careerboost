export const icons = {
    upload: "/assets/icons/upload.svg",
    dashboard: "/assets/icons/dashboard.svg",
    ai: "/assets/icons/ai.svg",
    settings: "/assets/icons/settings.svg",
    download: "/assets/icons/download.svg"
};

export function injectIcons() {
    document.querySelectorAll("[data-icon]").forEach(el => {
        const icon = el.getAttribute("data-icon");
        el.innerHTML = `<img src="${icons[icon]}" width="22" height="22"/>`;
    });
}
