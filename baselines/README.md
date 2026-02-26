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

# Baselines for [AAAI 26] TSBOW

In this section, we provide the Python source code for baseline models used in Experiments.


<!-- MARK: Installation -->

## 🔧 Installation

The experiments are based on [Ultralytics](https://github.com/ultralytics/ultralytics) and [YOLOv12](https://github.com/sunsmarterjie/yolov12). 
Please visit their installation guides for more detailed setup options.

1. For YOLOv8, YOLOv11, and RT-DETR models, we use the [Ultralytics](https://github.com/ultralytics/ultralytics) repo.

<details>
    <summary> Quick Installation </summary>

    ```bash
    bash install_ultralytics.sh
    ```

    or

    ```bash
    pip install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=11.8 -c pytorch -c nvidia
    git clone https://github.com/ultralytics/ultralytics 
    cd ultralytics 
    pip install -e .
    pip install tensorboard
    ```

</details>

<br>


2. For YOLOv12 model, we use the [YOLOv12](https://github.com/sunsmarterjie/yolov12) repo.

<details>
    <summary> Quick Installation </summary>

    ```bash
    bash install_yolov12.sh
    ```

    or

    ```bash
    git clone https://github.com/sunsmarterjie/yolov12 
    wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.3/flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl 
    conda create -n yolov12 python=3.11 -y 
    conda activate yolov12
    pip install -r requirements.txt
    pip install -e .
    ```

</details>

<br>


3. For manually labels, we use the [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling) tools. 
The installation and guideline are mentioned in [Documents](../documents/Document_XAnylabeling_ObjectDetection.pdf).

<details>
    <summary> Quick Installation </summary>

    ```bash
    bash install_Xanylabeling.sh
    ```
</details>



<!-- MARK: Training -->

## 🧑‍🏫 Training 

**YOLO**

[train_YOLO.py](train_YOLO.py) can be used for training the YOLOv8, YOLOv11, and YOLOv12 models.

The script below is an example for training the YOLO models on train set.

```bash
# for training multi-GPU
export NCCL_IB_GID_INDEX=3
export NCCL_P2P_DISABLE=1

python train_YOLO.py \
    -d 'NGOCHDM/Dataset/'   -n 'TSBOW'      -c '[0,1,2,3]'  \
    -m yolo11x    -e 100    -b 40           -i 1280         \
    --cache True            --state 'start'
```

The [bash file](train_YOLO.sh) can be executed via command:

```bash
bash train_YOLO.sh
```


**RT-DETR**

The script below is an example for training the RT-DETR model on train set.

```bash
# for training multi-GPU
export NCCL_IB_GID_INDEX=3
export NCCL_P2P_DISABLE=1

python train_RTDETR.py \
    -d 'NGOCHDM/Dataset/'   -n 'TSBOW'      -c '[0,1,2,3]' \
    -m 'rtdetr-x'     -e 100      -b 36   -i 1280
```

The [bash file](train_RTDETR.sh) can be executed via command:

```bash
bash train_RTDETR.sh
```



<!-- MARK: Validation -->

## 🔍 Validation

[validation.py](validation.py) can be used for validation the YOLOv8, YOLOv11, YOLOv12, and RT-DETR models.

The script below is an example for validating YOLOv12x on test set. More detailed validation configurations are mentioned in [validation.sh](validation.sh).

```bash
python validation.py \
    -d 'NGOCHDM/Dataset/'       -n 'TSBOW'          \
    -p 'runs/detect/'           -m "yolov12x_TSBOW" \
    -i 1280         -b 56       --conf 0.5          \
    --iou 0.6   --split 'test'  --max_det 300       \
    -r "EVALUATION/yolov12x_1280"
```

<!-- Results -->
Model performances after training 100 epochs and validating with imgsz=1280 on manually labeled test set.
| Method     | Precision | Recall    | mAP50     | mAP50–95  |
|:----------:|:---------:|:---------:|:---------:|:---------:|
| YOLOv8x    | 0.783     | 0.705     | 0.733     | 0.609     |
| YOLO11x    | 0.786     | 0.696     | 0.734     | 0.614     |
| YOLOv12x   | **0.806** | 0.662     | **0.744** | **0.615** |
| YOLO26x	 | 0.799     | 0.692     | 0.732	 | 0.61      |
| RT-DETR-x  | 0.731     | **0.740** | 0.718     | 0.552     |


<!-- Comparison with other datasets -->
<details>
    <summary>Comparison with other datasets</summary>

<div align="center" style="background:#ffffff; padding:11px; border-radius:10px; max-width:1000px; margin: 16px auto;">
    <img src="../images/Supp_Comparison_Performances.png" alt="TSBOW Comparison" style="width:100%; height:auto; border-radius:6px; display:block;">
</div>
<p align="center" style="margin:8px 0 0 0; font-weight:600;">Model performances when training on different datasets </p>

<div align="center" style="background:#ffffff; padding:5px; border-radius:10px; max-width:1000px; margin: 16px auto;">
    <img src="../images/Table_7.png" alt="TSBOW Comparison" style="width:100%; height:auto; border-radius:6px; display:block;">
</div>
<p align="center" style="margin:8px 0 0 0; font-weight:600;">Models performance for <i>car</i> across different metrics on <b>the comparison set</b> </p>

</details>



<!-- MARK: Inferences -->

<!-- ## 🤖 Inferences

**YOLOv12x** -->


<!-- MARK: Ablation -->

## 🔬 Ablation Studies

<!-- Ablation Studies -->
<details>
    <summary>Experiment Results</summary>

<div align="center" style="background:#f4f7fb; padding:3px; max-width:1000px; margin: 16px auto;">
    <img src="../images/Table_8_slide.png" alt="TSBOW Comparison" style="width:100%; height:auto; border-radius:6px; display:block;">
</div>
<p align="center" style="margin:8px 0 0 0; font-weight:600;">YOLOv12x performance across different classes. </p>

<div align="center" style="background:#f4f7fb; padding:3px; max-width:1000px; margin: 16px auto;">
    <img src="../images/Table_9_slide.png" alt="TSBOW Comparison" style="width:100%; height:auto; border-radius:6px; display:block;">
</div>
<p align="center" style="margin:8px 0 0 0; font-weight:600;">Influence of dataset characteristics on object detection performance.</p>

</details>


The [validation_ablation.sh](validation_ablation.sh) provides the validation process according to TSBOW metadata for each attributes.

The attributes are `classification = "SCENARIO WEATHER SCALE ROADTYPE TRAFFIC"`.


Attribute values:
```
class_sn_value = "road intersection specialcase disaster"
class_w_value  = "normal haze rain snow"
class_s_value  = "fine medium coarse"
class_r_value  = "urban standard boulevard"
class_t_value  = "light moderate heavy"
```


The script below is an example for validating the YOLOv12x model on **weather** category (test set). 

```bash
for weather in $class_w_value
do
    python validation.py \
        -d 'NGOCHDM/Dataset/'   -n 'TSBOW'   -y "TSBOWv01_WEATHER_${weather}"     \
        -p 'runs/detect/'       -m "ABLATION/yolov12x_TSBOW"                      \
        -c 'cuda:2'     -i 1280         -b 56               --max_det 300         \
        --conf 0.5      --iou 0.6       --split 'test'      --task "ablation"
done
```



<!-- MARK: Structures 🗃️-->

## 🗜️ Directory Structures for training models

```
TSBOW/
├─ train/
│  ├─ images/
│  └─ labels/
│
├─ val/
│  ├─ images/
│  └─ labels/
│
├─ test_public/
│  ├─ images/
│  └─ labels/
│
├─ classes.txt
├─ train.txt
├─ val.txt
├─ test_public.txt
└─ TSBOW.yaml
```


<!-- MARK: References -->

## 📚 References

Thanks to the developers and contributors of the following open-source repositories, whose invaluable work has greatly inspire our project:

- [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling): An open-source tool for precise bounding box creation.
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics): Detection models for training and real-time inferencing.
- [YOLOv12](https://github.com/sunsmarterjie/yolov12): A model for object detection.

Our repository is licensed under the **Apache 2.0 License**. However, if you use other components in your work, please follow their license.
