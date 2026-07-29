export function initHeader() {
    const headerLeft = document.querySelector(".header-left");
    if (headerLeft) {
        headerLeft.style.cursor = "pointer";
        headerLeft.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }

    const header = document.getElementById("scrollHeader");
    if (!header) {
        return;
    }

    let previousScrollPosition = window.scrollY;

    window.addEventListener("scroll", () => {
        const currentScrollPosition = window.scrollY;

        if (currentScrollPosition > 800) {
            header.style.top = "0";
        } else {
            header.style.top = "-116px";
        }

        previousScrollPosition = currentScrollPosition;
    });
}
