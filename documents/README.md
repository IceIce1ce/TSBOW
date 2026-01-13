# Documents








<!-- MARK: Datasets -->

## 📊 Datasets

<details>
    <summary>Comparison with other datasets</summary>

<!-- Image -->
<div align="center" style="background:#ffffff; padding:11px; border-radius:10px; max-width:1000px; margin: 16px auto;">
    <img src="../images/Supp_Datasets.png" alt="TSBOW Comparison" style="width:100%; height:auto; border-radius:6px; display:block;">
</div>
<p align="center" style="margin:8px 0 0 0; font-weight:600;">Comparison with other datasets about weather conditions and scales</p>

<!-- Table -->
<div align="center" style="background:#ffffff; padding:5px; border-radius:10px; max-width:1000px; margin: 16px auto;">
    <img src="../images/Table_1.png" alt="TSBOW Comparison" style="width:100%; height:auto; border-radius:6px; display:block;">
</div>
<p align="center" style="margin:8px 0 0 0; font-weight:600;">Comparison of traffic surveillance datasets </p>


</details> <br>

| Dataset           | Introduction                      |  Pub  | Paper |
|:---:              |:---                               | :---: | :--- |
| **UAVDT**         <br>[[website]](https://datasetninja.com/uavdt)| - *<span style="color: #FFCC00">Hardware</span>*: UAVs. <br> - *<span style="color: #33CCCC">Tasks</span>:* object detection, single object tracking, multiple-object tracking. <br> - *<span style="color: #FF6600">Position</span>:* China. <br> - *<span style="color: #6699FF">Weather</span>:* sunny/cloudy, fog, rain. <br> - *<span style="color: #FF0066">Time</span>:* day, night. | IJCV <br> 2020 | The Unmanned Aerial Vehicle Benchmark: Object Detection, Tracking and Baseline |
| **UA-DETRAC**     <br>[[website]](https://sites.google.com/view/daweidu/projects/ua-detrac?authuser=0)| - *<span style="color: #FFCC00">Hardware</span>*: Cannon EOS 550D camera. <br> - *<span style="color: #33CCCC">Tasks</span>:* object detection, multi-object tracking. <br> - *<span style="color: #FF6600">Position</span>:* China. <br> - *<span style="color: #6699FF">Weather</span>:* sunny/cloudy, rain. <br> - *<span style="color: #FF0066">Time</span>:* day, night. | CVIU <br> 2020 | UA-DETRAC: A new benchmark and protocol for multi-object detection and tracking |
| **AAU RainSnow**  <br>[[website]](https://vbn.aau.dk/en/datasets/aau-rainsnow-traffic-surveillance-dataset/)| - *<span style="color: #FFCC00">Hardware</span>*: RGB color and thermal camera. <br> - *<span style="color: #33CCCC">Tasks</span>:* instance segmentation, single object tracking, multiple-object tracking. <br> - *<span style="color: #FF6600">Position</span>:* Denmark. <br> - *<span style="color: #6699FF">Weather</span>:* fog, rain, snow. <br> - *<span style="color: #FF0066">Time</span>:* day, night. | ITS <br> 2019 | Rain Removal in Traffic Surveillance: Does it Matter? |
| 🎯 **<span style="color: #FFCC00">T</span><span style="color: #33CCCC">S</span><span style="color: #FF6600">B</span><span style="color: #6699FF">O</span><span style="color: #FF0066">W</span>**             <br>[[website]](https://skkuautolab.github.io/TSBOW/)| - *<span style="color: #FFCC00">Hardware</span>*: CCTV system + color camera. <br> - *<span style="color: #33CCCC">Tasks</span>:* object detection. <br> - *<span style="color: #FF6600">Position</span>:* South Korea. <br> - *<span style="color: #6699FF">Weather</span>:* sunny/cloudy, haze, rain, snow. <br> - *<span style="color: #FF0066">Time</span>:* day. <br> (night-time and other tasks will be updated later) | AAAI <br> 2026 | TSBOW: Traffic Surveillance Benchmark for Occluded Vehicles Under Various Weather Conditions |



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


## Licenses

Our repository on Github is licensed under the **Apache 2.0 License**. However, if you use other components in your work, please follow their license.

Our dataset on HuggingFace is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International** ([cc by-nc-nd 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.en)).