export function setTheme(theme) {
    const themeToggle = document.getElementById("themeToggle");
    if (!themeToggle) {
        return;
    }

    const isNight = theme === "night";

    document.body.classList.toggle("theme-night", isNight);
    localStorage.setItem("theme", theme);

    themeToggle.setAttribute(
        "aria-label",
        isNight ? "Switch to day theme" : "Switch to night theme"
    );
    themeToggle.setAttribute("aria-pressed", String(isNight));
}

export function initTheme() {
    const themeToggle = document.getElementById("themeToggle");
    if (!themeToggle) {
        return;
    }

    setTheme(localStorage.getItem("theme") || "day");

    themeToggle.addEventListener("click", () => {
        const nextTheme = document.body.classList.contains("theme-night")
            ? "day"
            : "night";

        setTheme(nextTheme);
    });
}
