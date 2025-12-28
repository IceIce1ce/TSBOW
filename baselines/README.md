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

In this section, we provide the Python source code for baseline models used in paper Experiments.


<!-- MARK: Installation -->

## 🔧 Installation

The experiments are based on [Ultralytics](https://github.com/ultralytics/ultralytics) and [YOLOv12](https://github.com/sunsmarterjie/yolov12). 
Please visit their installation guides for more detailed setup options.

1. For YOLOv8, YOLOv11, and RT-DETR models, we use the [Ultralytics](https://github.com/ultralytics/ultralytics) repo.

<details>
    <summary> Quick Installation </summary>

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



<!-- MARK: Training -->

## 🧑‍🏫 Training 

**YOLO**



**RT-DETR**



<!-- MARK: Validation -->

## ✔️ Validation




<!-- MARK: Inferences -->

<!-- ## 🧠 Inferences -->



<!-- MARK: References -->

## 📚 References

Thanks to the developers and contributors of the following open-source repositories, whose invaluable work has greatly inspire our project:

- [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling): An open-source tool for precise bounding box creation.
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics): Detection models for training and real-time inferencing.
- [YOLOv12](https://github.com/sunsmarterjie/yolov12): A model for object detection.

Our repository is licensed under the **Apache 2.0 License**. However, if you use other components in your work, please follow their license.
