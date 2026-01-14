# Documents


<!-- MARK: HF -->

## 🚗 TSBOW on HuggingFace

### Video Format

- Video Standard: mp4 (H.265)
- Video Resolution: 1280 x 720
- Video Frame Rate: varied from 20 to 30 FPS
- Videos are named as `<video_id>.mp4`


### Image Format

- Image Standard: jpg
- Image Resolution: 1280 x 720
- Images extracted from videos are named as `<video_id>_<frame_id>.jpg`. `<frame_id>` is 6 characters length.


### Ground Truth Format

Annotations are provided in YOLO format with one *.txt file per image. If there are no objects in an image, no *.txt file is required.
Each line in text file are the bounding box information of an object:

```
<class_id> <x_center> <y_center> <width> <height>
```

where
- `<class_id>` (int): class index starting from 0
- `x_center`, `y_center` (double): box coordinates normalized xywh format (from 0 to 1)
- `width`, `height` (double): box width, height


### Metadata Format

The [CSV file](metadata/TSBOW_info.csv) provides metadata for each videos, including: scenario, daytime, weather, scale, roadtype, video_id, total_duration, and ROI zone. 

- `SCENARIO` (char): one of four values: `r` (road), `i` (intersection), `s` (special cases), `d` (disaster).
- `DAYTIME` (char): `d` (day), `n` (night).
- `WEATHER` (char): one of four values: `n` (normal), `h` (haze), `r` (rain), `s` (snow).
- `SCALE` (char): one of three values: `f` (fine), `m` (medium), `c` (coarse).
- `ROADTYPE` (char): one of three values: `u` (urban), `s` (standard), `b` (boulevard).
- `VIDEO_ID` (string): video name.
- `DURATION` (duration): total duration of whole videos (test + val + train). 
- `ROI` (string): a list of points in polygon.


### Directory Structure

- **Train/Val/Test_Public**: 
    - `videos.zip`: video files. 
    - `annotations.zip`: annotations include images and labels.
    - `semilabels.zip`: semi-labeled annotations include labels only. You can extract frames from videos.
    - Notes for Test_Public: In the first publication, we only public annotations of the last 30% of test set. The remaining files will be public in the future.

- **Others**:
    - `comparison.zip`: annotations of datasets' comparison in Experiment section, include images and labels.
    - `TSBOW_info.csv`: metadata file.



<!-- MARK: Datasets -->

## 📊 Datasets

<!-- Colapsed content -->
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


<!-- Comparison Table -->

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



<!-- MARK: License -->

## 🔑 Licenses

Our repository on Github is licensed under the **Apache 2.0 License**. However, if you use other components in your work, please follow their license.

Our dataset on HuggingFace is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International** ([cc by-nc-nd 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.en)).