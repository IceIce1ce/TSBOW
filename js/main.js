import { initTitleSync } from "./title-sync.js";
import { initHeader } from "./header.js";
import { filterScenes, showImage, showVideo } from "./scenes.js";
import { copyBibtex } from "./citation.js";
import { initTheme, setTheme } from "./theme.js";

initTitleSync();
initHeader();
initTheme();

// These functions are used by inline onclick handlers in the HTML pages.
window.filterScenes = filterScenes;
window.showImage = showImage;
window.showVideo = showVideo;
window.copyBibtex = copyBibtex;
window.setTheme = setTheme;
