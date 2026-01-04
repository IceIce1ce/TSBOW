// base_url = "https://huggingface.co/datasets/skku-autolab/TSBOW"

// MARK: Title - Synchronize hover 
document.addEventListener('DOMContentLoaded', function() 
{
  const t1_T = document.querySelector('#tsbow-title .sync-tsbowT');
  const t2_T = document.querySelector('#titleText .sync-tsbowT');
  if (t1_T && t2_T) 
  {
    function addHighlight() 
    {
      t1_T.classList.add('highlight');
      t2_T.classList.add('highlight');
    }
    function removeHighlight() 
    {
      t1_T.classList.remove('highlight');
      t2_T.classList.remove('highlight');
    }
    t1_T.addEventListener('mouseenter', addHighlight);
    t1_T.addEventListener('mouseleave', removeHighlight);
    t2_T.addEventListener('mouseenter', addHighlight);
    t2_T.addEventListener('mouseleave', removeHighlight);
  }

  const t1_S = document.querySelector('#tsbow-title .sync-tsbowS');
  const t2_S = document.querySelector('#titleText .sync-tsbowS');
  if (t1_S && t2_S) 
  {
    function addHighlight() 
    {
      t1_S.classList.add('highlight');
      t2_S.classList.add('highlight');
    }
    function removeHighlight() 
    {
      t1_S.classList.remove('highlight');
      t2_S.classList.remove('highlight');
    }
    t1_S.addEventListener('mouseenter', addHighlight);
    t1_S.addEventListener('mouseleave', removeHighlight);
    t2_S.addEventListener('mouseenter', addHighlight);
    t2_S.addEventListener('mouseleave', removeHighlight);
  }
  
  const t1_B = document.querySelector('#tsbow-title .sync-tsbowB');
  const t2_B = document.querySelector('#titleText .sync-tsbowB');
  if (t1_B && t2_B) {
    function addHighlight() {
      t1_B.classList.add('highlight');
      t2_B.classList.add('highlight');
    }
    function removeHighlight() {
      t1_B.classList.remove('highlight');
      t2_B.classList.remove('highlight');
    }
    t1_B.addEventListener('mouseenter', addHighlight);
    t1_B.addEventListener('mouseleave', removeHighlight);
    t2_B.addEventListener('mouseenter', addHighlight);
    t2_B.addEventListener('mouseleave', removeHighlight);
  }
  
  const t1_O = document.querySelector('#tsbow-title .sync-tsbowO');
  const t2_O = document.querySelector('#titleText .sync-tsbowO');
  if (t1_O && t2_O) {
    function addHighlight() {
      t1_O.classList.add('highlight');
      t2_O.classList.add('highlight');
    }
    function removeHighlight() {
      t1_O.classList.remove('highlight');
      t2_O.classList.remove('highlight');
    }
    t1_O.addEventListener('mouseenter', addHighlight);
    t1_O.addEventListener('mouseleave', removeHighlight);
    t2_O.addEventListener('mouseenter', addHighlight);
    t2_O.addEventListener('mouseleave', removeHighlight);
  }
  
  const t1_W = document.querySelector('#tsbow-title .sync-tsbowW');
  const t2_W = document.querySelector('#titleText .sync-tsbowW');
  if (t1_W && t2_W) {
    function addHighlight() {
      t1_W.classList.add('highlight');
      t2_W.classList.add('highlight');
    }
    function removeHighlight() {
      t1_W.classList.remove('highlight');
      t2_W.classList.remove('highlight');
    }
    t1_W.addEventListener('mouseenter', addHighlight);
    t1_W.addEventListener('mouseleave', removeHighlight);
    t2_W.addEventListener('mouseenter', addHighlight);
    t2_W.addEventListener('mouseleave', removeHighlight);
  }

  // Highlight all title letters when hovering the main page logo
  const pageLogo = document.querySelector('img[src*="TSBOW_icon_white_BG.png"]');
  const letterSelectors = '.sync-tsbowT, .sync-tsbowS, .sync-tsbowB, .sync-tsbowO, .sync-tsbowW';
  if (pageLogo) {
    const letters = document.querySelectorAll(letterSelectors);
    pageLogo.addEventListener('mouseenter', () => {
      letters.forEach(el => el.classList.add('highlight'));
    });
    pageLogo.addEventListener('mouseleave', () => {
      letters.forEach(el => el.classList.remove('highlight'));
    });
  }
});


// MARK: header - scroll to top on logo/TSBOW click
const headerLeft = document.querySelector(".header-left");
if (headerLeft) 
{
  headerLeft.style.cursor = "pointer";
  headerLeft.addEventListener("click", () => {
      window.scrollTo({
          top: 0,
          behavior: "smooth"
      });
  });
}

// header
const header = document.getElementById("scrollHeader");
let prevScrollPos = window.scrollY;

window.addEventListener("scroll", () => {
const currentScrollPos = window.scrollY;

if (currentScrollPos > 800) // 👈 only start showing after 800px down
{ 
    if (prevScrollPos > currentScrollPos) 
    {
      header.style.top = "0";       // show when scrolling up
    } 
    else 
    {
      header.style.top = "0";   // -80px if need hide when scrolling down
    }
} 
else 
{
    header.style.top = "-116px";     // stay hidden near the top
}

prevScrollPos = currentScrollPos;
});


// MARK: Scenes
const subvalues = {
    "SCENARIO": ["road", "intersection", "specialcase", "disaster"],
    "WEATHER":  ["normal", "haze", "rain", "snow"],
    "SCALE":    ["fine", "medium", "coarse"],
    "ROADTYPE": ["urban", "standard", "boulevard"],
    "TRAFFIC":  ["light", "moderate", "heavy"]
};

const filterColors = {
    "ALL":      "#FFCC00",
    "SCENARIO": "#33CCCC",
    "WEATHER":  "#FF6600",
    "SCALE":    "#FF0066",
    "ROADTYPE": "#6699FF",
    "TRAFFIC":  "#33CCFF"
};

function filterScenes(filter) {
    const subvaluesContainer = document.querySelector('.filter-subvalues');
    const visualizationContainer = document.querySelector('.filter-visualization');
    const visualizationImage = document.getElementById('visualization-image');
    const visualizationVideo = document.getElementById('visualization-video');
    const videoSource = document.getElementById('video-source');

    // Clear existing sub-value buttons
    subvaluesContainer.innerHTML = '';

    // Reset visualization
    visualizationContainer.style.display = 'none';
    visualizationImage.style.display = 'none';
    visualizationVideo.style.display = 'none';
    videoSource.src = '';

    // Show the image only for "ALL"
    if (filter === 'ALL') {
        visualizationContainer.style.display = 'block';
        visualizationImage.src = `images/TSBOW_scenes.jpg`;
        visualizationImage.style.display = 'block';
    }

    // Add sub-value buttons for the selected filter
    if (subvalues[filter]) {
        subvalues[filter].forEach(subvalue => {
            const button = document.createElement('button');
            button.className = 'btn subvalue-btn';
            button.style = `padding: 10px 20px; margin: 5px; background-color: ${filterColors[filter]}; color: #001F3F;`;
            button.textContent = subvalue.toUpperCase();
            // button.onclick = () => showVideo(filter, subvalue);
            button.onclick = () => showImage(filter, subvalue);
            subvaluesContainer.appendChild(button);
        });
    }
}

function showImage(filter, subvalue) {
    const visualizationContainer = document.querySelector('.filter-visualization');
    const visualizationImage = document.getElementById('visualization-image');
    const visualizationVideo = document.getElementById('visualization-video');

    const imagePath = `images/${filter}_${subvalue}.jpg`;

    // Hide the video and show the image
    visualizationVideo.style.display = 'none';
    visualizationImage.style.display = 'block';
    visualizationImage.src = imagePath;

    // Check if the image file exists
    visualizationImage.onload = () => {
        console.log(`Image successfully loaded: ${imagePath}`);
        visualizationContainer.style.display = 'block'; // Ensure the container is visible
    };
    
    // Handle image load error
    visualizationImage.onerror = () => {
        console.error(`Error: Image not found at path: ${imagePath}`);
        visualizationImage.style.display = 'none'; // Hide the image if it doesn't exist
    };

    // Log the final image source
    console.log(`Image source set to: ${visualizationImage.src}`);
}

function showVideo(filter, subvalue) {
    const visualizationContainer = document.querySelector('.filter-visualization');
    const visualizationImage = document.getElementById('visualization-image');
    const visualizationVideo = document.getElementById('visualization-video');
    const videoSource = document.getElementById('video-source');

    // Hide the image and show the video
    visualizationImage.style.display = 'none';
    visualizationVideo.style.display = 'block';
    videoSource.src = `videos/${filter}_${subvalue}.mp4`;
    visualizationVideo.load();
    visualizationVideo.play();
}


// MARK: citation
function copyBibtex() {
  const code = document.querySelector("#citation pre code").innerText;
  navigator.clipboard.writeText(code);
  const btn = document.querySelector(".copy-btn");
  btn.innerText = "✅ Copied!";
  setTimeout(() => btn.innerText = "📋 Copy", 2000);
}



// MARK: footer
const footer = document.getElementById("dynamicFooter");

window.addEventListener("scroll", () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 10) {
        // footer.classList.add("visible");
    } else {
        // footer.classList.remove("visible");
    }
});




// MARK: Notice

document.querySelectorAll(".coming-soon").forEach(link =>{
    link.addEventListener("click", e=>{
        e.preventDefault();
        showNotice("This page will be available in a future update");
    });
});

