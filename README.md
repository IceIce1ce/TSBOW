<!-- 
__        _______ _     ____ ___  __  __ _____ 
\ \      / / ____| |   / ___/ _ \|  \/  | ____|
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
  \ V  V / | |___| |__| |__| |_| | |  | | |___ 
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|
                                   
 _____ ___  
|_   _/ _ \ 
  | || | | |
  | || |_| |
  |_| \___/ 
            

 _____ ____  ____   _____        __
|_   _/ ___|| __ ) / _ \ \      / /
  | | \___ \|  _ \| | | \ \ /\ / / 
  | |  ___) | |_) | |_| |\ V  V /  
  |_| |____/|____/ \___/  \_/\_/   
                                   
-->
                              

<h1 align='center'>
    TSBOW: Traffic Surveillance Benchmark<br> for Occluded Vehicles
    <br> Under Various Weather Conditions
</h1>


<!-- MARK: authors -->
<div align='center'>
    <a href="https://scholar.google.com/citations?user=pCTUkWwAAAAJ">
        Ngoc Doan-Minh Huynh</a> &emsp;
    <a href="https://scholar.google.com/citations?user=crRQGUAAAAAJ">
        Duong Nguyen-Ngoc Tran</a> &emsp;
    <a href="https://scholar.google.com/citations?user=xPyle9AAAAAJ">
        Long Hoang Pham</a>   
</div>

<div align='center'>
    Tai Huu-Phuong Tran &emsp;
    Hyung-Joon Jeon     &emsp;
    Huy-Hung Nguyen     &emsp;
    Duong Khac Vu       &emsp;
    Hyung-Min Jeon      
</div>

<div align='center'>
    Son Hong Phan       &emsp; 
    Quoc Pham-Nam Ho    &emsp;
    Chi Dai Tran        &emsp;
    Trinh Le Ba Khanh   &emsp;
    <a href="https://scholar.google.com/citations?user=9z0SfKoAAAAJ">
        Jae Wook Jeon</a>
</div>


<!-- affliation -->
<div align='center'>
    <a href="https://micro.skku.ac.kr/micro/index.do">Automation Lab</a>, Sungkyunkwan University
</div>

<br>

<div align='center'>
    <b>Corresponding Author</b>: jwjeon@skku.edu
    <br>
    <b>Contact for Dataset</b>: jwjeon@skku.edu, ngochdm@skku.edu, automation.skku@gmail.com
</div>


<!-- MARK: URLs -->
<!-- get img shields at: -->
<!-- https://shields.io/badges -->
<!-- check icon at: -->
<!-- https://github.com/simple-icons/simple-icons/blob/master/slugs.md  -->
<br> 

<div align="center">
  <a href="https://skkuautolab.github.io/TSBOW/"><img src="https://img.shields.io/static/v1?label=TSBOW&message=Website&color=9a33fc&logo=githubpages" style="height: 25px;"></a>  
  <a href="https://ojs.aaai.org/index.php/AAAI/article/view/37439"><img src="https://img.shields.io/static/v1?label=DOI&message=10.1609/aaai.v40i7.37439&color=green" style="height: 25px;"></a>  
  <a href="https://arxiv.org/abs/2602.05414"><img src="https://img.shields.io/static/v1?label=Supplementary&message=arXiv&color=FF0066&logo=arxiv" style="height: 25px;"></a>  
  <br>
  <!-- <a href="https://docs.google.com/presentation/d/1Wd2alQk565YBZjTaoVdSrdDacb_ILhlXTOzTTP_tTt4/edit?usp=sharing"><img src="https://img.shields.io/static/v1?label=Slides&message=Presentation&color=fa9f1b&logo=googleslides" style="height: 25px;"></a>    -->
  <a href="https://github.com/SKKUAutoLab/TSBOW"><img src="https://img.shields.io/static/v1?label=Code&message=Github&color=6699FF&logo=github" style="height: 25px;"></a>   
  <a href="https://huggingface.co/datasets/SKKUAutoLab/TSBOW"><img src="https://img.shields.io/static/v1?label=Dataset&message=HuggingFace&color=FF6600&logo=huggingface" style="height: 25px;"></a>  
</div>

<br>


![TSBOW Dataset Scenes](images/Figure_All_Scenes.png)


<!-- MARK: News -->

## 🎉 NEWS

<!-- + [2025.12.31] 🔥 Our paper, code and TSBOW dataset are released! -->

+ [2026.01.16] 🎆 TSBOW dataset is available on HuggingFace.
+ [2025.11.16] 🔥 Our code and website are released!
+ [2025.11.08] 🎉 **<span style="color: #FFCC00">T</span><span style="color: #33CCCC">S</span><span style="color: #FF6600">B</span><span style="color: #6699FF">O</span><span style="color: #FF0066">W</span>** has been accepted to **AAAI 2026**!


<!-- MARK: Abstract -->

## 📝 Abstract

Global warming has intensified the frequency and severity of extreme weather events, which degrade CCTV signal and video quality while disrupting traffic flow, thereby increasing traffic accident rates. Existing datasets, often limited to light haze, rain, and snow, fail to capture extreme weather conditions. To address this gap, this study introduces the **T**raffic **S**urveillance **B**enchmark for **O**ccluded Vehicles under Various **W**eather Conditions (**TSBOW**), a comprehensive dataset designed to enhance occluded vehicle detection across diverse annual weather scenarios. Comprising over **32 hours** of real-world traffic data from densely populated urban areas, TSBOW includes more than **48,000 manually annotated** and **3.2 million semi-labeled frames**; bounding boxes spanning eight traffic participant classes from large vehicles to micromobility devices and pedestrians. We establish an object detection benchmark for TSBOW, highlighting challenges posed by occlusions and adverse weather. With its varied road types, scales, and viewpoints, TSBOW serves as a critical resource for advancing Intelligent Transportation Systems. Our findings underscore the potential of CCTV-based traffic monitoring, paving the way for new research and applications. The TSBOW dataset is publicly available at the following link. <br>
**Code** -- https://github.com/SKKUAutoLab/TSBOW



<!-- MARK: Overview -->

## 🌍 Overview

<div align="center" style="max-width:900px; margin: 10px auto 20px; border-radius: 8px;">
    <img src="images/Github_StatsTable_1x6.png" alt="TSBOW Stats" style="width:100%; height:auto; display:block; border-radius:6px;">
    <p><b>Dataset Statistics</b></p>
</div>

<div align="center" style="max-width:900px; margin: 10px auto 20px; border-radius: 8px;">
    <img src="images/Chart_SunburstChart_Attributes.png" alt="Video Distribution" style="width:70%; height:auto; display:block; border-radius:6px;">
    <p><b>Video Distribution</b></p>
</div>

<!-- <div align="center" style="max-width:1000px; margin: 10px auto 20px;">
    <div style="display:flex; gap:18px; justify-content:center; align-items:flex-start; flex-wrap:wrap;">
        <div style="flex:1 1 440px; max-width:51%; text-align:center;">
            <img src="images/Figure_Suwon_Camera_Map.png" alt="Recording Locations" style="width:100%; height:auto; display:block; border-radius:6px;">
            <p style="margin:8px 0 0 0; font-weight:600;">Recording Locations</p>
        </div>
        <div style="flex:1 1 440px; max-width:42%; text-align:center;">
            <img src="images/Chart_SunburstChart_Attributes.png" alt="Video Distribution" style="width:100%; height:auto; display:block; border-radius:6px;">
            <p style="margin:8px 0 0 0; font-weight:600;">Video Distribution</p>
        </div>
    </div>
</div> -->

<details>
    <summary>Other Distributions</summary>

<!-- Class Distribution -->
<div align="center" style="max-width:900px; margin: 10px auto 20px; border-radius: 8px;">
    <img src="images/Chart_TSBOW_ClassDist.png" alt="Class Dist" style="width:100%; height:auto; display:block; border-radius:6px;">
    <p><b>Class Distribution</b></p>
</div>

<!-- Occlusion and Traffic Distribution -->
<div align="center" style="max-width:1000px; margin: 10px auto 20px;">
    <div style="display:flex; gap:18px; justify-content:center; align-items:flex-start; flex-wrap:wrap;">
        <div style="flex:1 1 440px; max-width:48%; text-align:center;">
            <img src="images/Chart_TSBOW_Occlusion.png" alt="chart occlusion" style="width:100%; height:auto; display:block; border-radius:6px;">
            <p style="margin:8px 0 0 0; font-weight:600;">Occlusion Ditribution</p>
        </div>
        <div style="flex:1 1 440px; max-width:45%; text-align:center;">
            <img src="images/Chart_TSBOW_Traffic.png" alt="chart traffic" style="width:100%; height:auto; display:block; border-radius:6px;">
            <p style="margin:8px 0 0 0; font-weight:600;">Traffic Distribution</p>
        </div>
    </div>
</div>

</details>

<!-- Table 2x3 for github -->
<!-- <div align="center">
    <table style="width: 100%; max-width: 800px; margin: 30px auto; border-collapse: collapse;">
        <tr>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #33CCCC; font-weight: bold;">198</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #33CCCC; font-weight: bold;">📹 Processed Videos 📹</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #FFCC00; font-weight: bold;">32 h</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #FFCC00; font-weight: bold;">⏱️ Duration ⏱️</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #6699FF; font-weight: bold;">3.2 M</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #6699FF; font-weight: bold;">🖼️ Total Frames 🖼️</p>
            </td>
        </tr>
        <tr>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #FF6600; font-weight: bold;">71.1 M</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #FF6600; font-weight: bold;">Semi-Annotated<br>Instances</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #33CCFF; font-weight: bold;">48 K</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #33CCFF; font-weight: bold;">Manual-Annotated<br>Frames</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #FF0066; font-weight: bold;">1.1 M</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #FF0066; font-weight: bold;">Manual-Anotated<br>Instances</p>
            </td>
        </tr>
    </table>
</div> -->

<!-- Table 1x6 for poster -->
<!-- <div align="center">
    <table style="width: 100%; max-width: 1100px; margin: 30px auto; border-collapse: collapse;">
        <tr>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #33CCCC; font-weight: bold;">198</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #33CCCC; font-weight: bold;">Processed Videos<br>📹</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #FFCC00; font-weight: bold;">32 h</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #FFCC00; font-weight: bold;">Duration<br>⏱️</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #6699FF; font-weight: bold;">3.2 M</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #6699FF; font-weight: bold;">Total Frames<br>🖼️</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #FF6600; font-weight: bold;">71.1 M</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #FF6600; font-weight: bold;">Semi-Annotated<br>Instances</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #33CCFF; font-weight: bold;">48 K</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #33CCFF; font-weight: bold;">Manual-Annotated<br>Frames</p>
            </td>
            <td style="padding: 25px 15px; text-align: center; border: 1px solid #ddd; background: #092030;">
                <h2 style="margin: 0; font-size: 2.5em; color: #FF0066; font-weight: bold;">1.1 M</h2>
                <p style="margin: 8px 0 0 0; font-size: 1.1em; color: #FF0066; font-weight: bold;">Manual-Anotated<br>Instances</p>
            </td>
        </tr>
    </table>
</div> -->



<!-- MARK: Datasets -->

## 📊 Benchmark Datasets


**TSBOW** Introduction
- *<span style="color: #FFCC00">Hardware</span>*: CCTV system + color camera. 
- *<span style="color: #33CCCC">Tasks</span>:* object detection. 
- *<span style="color: #FF6600">Position</span>:* South Korea. 
- *<span style="color: #6699FF">Weather</span>:* sunny/cloudy, haze, rain, snow. 
- *<span style="color: #FF0066">Time</span>:* day.

Our data formats are described in [TSBOW on HuggingFace](documents/README.md#-tsbow-on-huggingface) section.

The comparison between different datasets are described in [Datasets](documents/README.md#-datasets) section.

The demo videos are provided in [TSBOW Scenes](https://skkuautolab.github.io/TSBOW/TSBOW_scenes.html). The UI for filtering scenes is provided in [Releases: TSBOW-Filter-Scenes_v1.1](https://github.com/SKKUAutoLab/TSBOW/releases/tag/FS_v1.1) on this repo.


<!-- MARK: Baselines -->

## 📈 Baselines

|  Year |  Pub    | Paper                            | Link  | Note |
| :---: |  :---:  | :---                             |:---:  | :--- |
| 2024  |  ICDICI | A review on yolov8 and its advancements | [paper](https://link.springer.com/chapter/10.1007/978-981-99-7962-2_39) | YOLOv8 |
| 2024  |  arXiV  | YOLOv11: An Overview of the Key Architectural Enhancements | [paper](https://arxiv.org/abs/2410.17725) | YOLOv11 |
| 2024  |  CVPR   | DETRs Beat YOLOs on Real-time Object Detection | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_DETRs_Beat_YOLOs_on_Real-time_Object_Detection_CVPR_2024_paper.html) | RT-DETR |
| 2025  |  arXiV  | A Breakdown of the Key Architectural Features | [paper](https://arxiv.org/abs/2502.14740) | YOLOv12 |
| 2025  |  arXiV  | YOLO26: Key Architectural Enhancements and Performance Benchmarking for Real-Time Object Detection | [paper](https://arxiv.org/abs/2509.25164) | YOLO26 |


The source codes for baseline models are provided in [Baselines](baselines/) folder. 
Read [Instruction](baselines/README.md) for more information.



<!-- MARK: Metrics -->

<!-- ## ⚖️ Metrics -->

<!-- | Metric        | Abbr      | Reference         | Link      |
| :---:         | :---:     | :---:             | :---      | -->



<!-- MARK: Experiments -->

## 🔬 Experiments


<!-- Validation Methods - Visualization -->
<div align="center" style="background:#ffffff; padding:11px; border-radius:10px; max-width:1000px; margin: 16px auto;">
    <img src="images/Supp_Models_Performances.png" alt="TSBOW Experiments" style="width:100%; height:auto; border-radius:6px; display:block;">
</div>
<p align="center" style="margin:8px 0 0 0; font-weight:600;"> Model performances under different weather conditions </p>


<!-- Ablation Study -->
The source code for validating Ablation Studies are provided in [validation_ablation.sh](baselines/validation_ablation.sh). Please read the [Instruction](baselines/README.md) for the experiment results and more information.



<!-- MARK: Download -->

## 📥 Dataset Download

The **<span style="color: #FFCC00">T</span><span style="color: #33CCCC">S</span><span style="color: #FF6600">B</span><span style="color: #6699FF">O</span><span style="color: #FF0066">W</span>** dataset is distributed under the <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.en"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International</a> License. 

By completing the form below, users acknowledge and agree that <b>the dataset will be used solely for research purposes</b>. 

<details>
    <summary><b>Submission Guidelines</b></summary>

<b>1. TSBOW - Terms and Conditions Form</b>
- Download and fill out the <a href="https://docs.google.com/document/d/1Mn4qV8HErCX1EMQvys6SAKbMb06dZa85nie7rzSxeGc/edit?usp=sharing"> TSBOW - Terms and Conditions</a> form. 
- Ensure all **User Information** fields are completed.
- Provide a description of your intended use of the dataset.
- Check the agreement box and insert your handwritten signature.
- Save as PDF file. Renaming as: **{TSBOW}_{Application-Date}_{Huggingface-Username}.pdf** (i.e. TSBOW_20260120_ngochdm.pdf)

<b>2. Requirement Email</b>
- The subject format: [TSBOW Access Requirement] {Your Name} - {Affiliation}
- The email body includes your <b>HuggingFace account information</b> (username and email). We will verify this information against the access requirements on Hugging Face before approval.
- Send email to all our addresses: <b>jwjeon@skku.edu, ngochdm@skku.edu, automation.skku@gmail.com</b>

<b>3. Send Request on HuggingFace</b>
- Press "Agree and send request to access TSBOW" button <a href="https://huggingface.co/datasets/SKKUAutoLab/TSBOW">on HuggingFace</a>. Our team may take 2-3 days to process your request.

</details>
<br>

Scripts to download **<span style="color: #FFCC00">T</span><span style="color: #33CCCC">S</span><span style="color: #FF6600">B</span><span style="color: #6699FF">O</span><span style="color: #FF0066">W</span>** from HuggingFace are provided in [utils](utils/README.md) folder. Please refer to the [`download_TSBOW.py`](utils/download_TSBOW.py) and [`download_TSBOW.sh`](utils/download_TSBOW.sh) for more details.


<!-- MARK: References -->

## 📚 References

Thanks to the developers and contributors of the following open-source repositories, whose invaluable work has greatly inspire our project:

**Datasets**:
- [UAVDT](https://datasetninja.com/uavdt): A traffic dataset contains drone footages under sunny and rainy conditions.
- [UA-DETRAC](https://wayback.archive-it.org/org-652/20231112205116/https:/detrac-db.rit.albany.edu/): A traffic surveillance dataset captures sunny and rainy weather.
- [AAU RainSnow](https://vbn.aau.dk/en/datasets/aau-rainsnow-traffic-surveillance-dataset/): A traffic surveillance dataset provides segmentation annotations for rain and snow weather.
<!-- new UA-DETRAC website: https://sites.google.com/view/daweidu/projects/ua-detrac?authuser=0 -->

**Github Repo**:
- [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling): An open-source tool for precise bounding box creation.
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics): Detection models for training and real-time inferencing.
- [YOLOv12](https://github.com/sunsmarterjie/yolov12): A model for object detection.

Our repository is licensed under the **Apache 2.0 License**. However, if you use other components in your work, please follow their license.



<!-- MARK: Citation -->

## 🏅 Citation

**If our research is helpful to you, please cite our paper using the following BibTeX format**

We will update the citation again after the AAAI-26 proceedings publication.

```bibtex
@misc{huynh2026tsbowtrafficsurveillancebenchmark,
      title={TSBOW: Traffic Surveillance Benchmark for Occluded Vehicles Under Various Weather Conditions}, 
      author={Ngoc Doan-Minh Huynh and Duong Nguyen-Ngoc Tran and Long Hoang Pham and Tai Huu-Phuong Tran and Hyung-Joon Jeon and Huy-Hung Nguyen and Duong Khac Vu and Hyung-Min Jeon and Son Hong Phan and Quoc Pham-Nam Ho and Chi Dai Tran and Trinh Le Ba Khanh and Jae Wook Jeon},
      year={2026},
      eprint={2602.05414},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2602.05414}, 
}
```


<!-- MARK: Git Stats -->

<!-- ![Star History Chart](https://api.star-history.com/svg?repos=SKKUAutoLab/TSBOW&type=Date) -->

<!-- ![](https://img.shields.io/github/downloads/SKKUAutoLab/TSBOW/total.svg?style=for-the-badge) -->

<!-- <div style="position: relative; display: inline-block;">
  <img src="https://api.star-history.com/svg?repos=SKKUAutoLab/TSBOW&type=Date" alt="Star History Graph">
  <img src="icons/TSBOW_icon_white_BG.png" style="position: absolute; top: 10px; left: 310px; width: 30px; height: 30px;" alt="Custom Avatar">
</div> -->

<div align="center"><a href="#top">🔝 Back to Top</a></div>




<!-- https://search.google.com/search-console/ownership?resource_id=https%3A%2F%2Fskkuautolab.github.io%2FTSBOW%2F -->
<!-- figlet -->