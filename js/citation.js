export function copyBibtex() {
    const code = document.querySelector("#citation pre code").innerText;
    navigator.clipboard.writeText(code);

    const button = document.querySelector(".copy-btn");
    button.innerText = "✅ Copied!";
    setTimeout(() => button.innerText = "📋 Copy", 2000);
}
