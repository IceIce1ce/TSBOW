const titleLetters = ["T", "S", "B", "O", "W"];

export function initTitleSync() {
    titleLetters.forEach(letter => {
        const titleLetter = document.querySelector(`#tsbow-title .sync-tsbow${letter}`);
        const textLetter = document.querySelector(`#titleText .sync-tsbow${letter}`);

        if (!titleLetter || !textLetter) {
            return;
        }

        const setHighlight = highlighted => {
            titleLetter.classList.toggle("highlight", highlighted);
            textLetter.classList.toggle("highlight", highlighted);
        };

        titleLetter.addEventListener("mouseenter", () => setHighlight(true));
        titleLetter.addEventListener("mouseleave", () => setHighlight(false));
        textLetter.addEventListener("mouseenter", () => setHighlight(true));
        textLetter.addEventListener("mouseleave", () => setHighlight(false));
    });

    // Highlight all title letters when hovering the main page logo.
    const pageLogo = document.querySelector('img[src*="TSBOW_icon_no_BG_white_border.png"]');
    if (!pageLogo) {
        return;
    }

    const letters = document.querySelectorAll(
        ".sync-tsbowT, .sync-tsbowS, .sync-tsbowB, .sync-tsbowO, .sync-tsbowW"
    );

    pageLogo.addEventListener("mouseenter", () => {
        letters.forEach(letter => letter.classList.add("highlight"));
    });
    pageLogo.addEventListener("mouseleave", () => {
        letters.forEach(letter => letter.classList.remove("highlight"));
    });
}
