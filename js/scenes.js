const attributeValues = {
    SCENARIO: ["road", "intersection", "specialcase", "disaster"],
    WEATHER: ["normal", "haze", "rain", "snow"],
    SCALE: ["fine", "medium", "coarse"],
    ROADTYPE: ["urban", "standard", "boulevard"],
    TRAFFIC: ["light", "moderate", "heavy"]
};

const attributeEmojis = {
    ALL: "✨",
    SCENARIO: "🚦",
    WEATHER: "🌦️",
    SCALE: "🔎",
    ROADTYPE: "🛣️",
    TRAFFIC: "🚗"
};

export function filterScenes(attributeName) {
    const attributeValuesContainer = document.querySelector(".filter-attributes");
    const visualizationContainer = document.querySelector(".filter-visualization");
    const visualizationImage = document.getElementById("visualization-image");
    const visualizationVideo = document.getElementById("visualization-video");
    const videoSource = document.getElementById("video-source");

    // Clear existing sub-value buttons.
    attributeValuesContainer.innerHTML = "";

    // Reset visualization.
    visualizationContainer.style.display = "none";
    visualizationImage.style.display = "none";
    visualizationVideo.style.display = "none";
    videoSource.src = "";

    if (attributeName === "ALL") {
        visualizationContainer.style.display = "block";
        visualizationImage.src = "images/TSBOW_scenes.jpg";
        visualizationImage.style.display = "block";
    }

    if (!attributeValues[attributeName]) {
        return;
    }

    attributeValues[attributeName].forEach(attributeValue => {
        const button = document.createElement("button");
        button.className = "btn subvalue-btn";
        button.style = "padding: 10px 20px; margin: 5px; background-color: #000080; color: #FFFFFF;";
        button.textContent = `${attributeEmojis[attributeName]} ${attributeValue.toUpperCase()}`;
        button.onclick = () => showImage(attributeName, attributeValue);
        attributeValuesContainer.appendChild(button);
    });
}

export function showImage(attributeName, attributeValue) {
    const visualizationContainer = document.querySelector(".filter-visualization");
    const visualizationImage = document.getElementById("visualization-image");
    const visualizationVideo = document.getElementById("visualization-video");
    const imagePath = `images/${attributeName}_${attributeValue}.jpg`;

    visualizationVideo.style.display = "none";
    visualizationImage.style.display = "block";
    visualizationImage.src = imagePath;

    visualizationImage.onload = () => {
        console.log(`Image successfully loaded: ${imagePath}`);
        visualizationContainer.style.display = "block";
    };

    visualizationImage.onerror = () => {
        console.error(`Error: Image not found at path: ${imagePath}`);
        visualizationImage.style.display = "none";
    };

    console.log(`Image source set to: ${visualizationImage.src}`);
}

export function showVideo(attributeName, attributeValue) {
    const visualizationImage = document.getElementById("visualization-image");
    const visualizationVideo = document.getElementById("visualization-video");
    const videoSource = document.getElementById("video-source");

    visualizationImage.style.display = "none";
    visualizationVideo.style.display = "block";
    videoSource.src = `videos/${attributeName}_${attributeValue}.mp4`;
    visualizationVideo.load();
    visualizationVideo.play();
}
