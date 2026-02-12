
echo "Create & activate yolov12 environment before installation"

echo "     create: conda create -n yolov12  python=3.11 -y"

echo "     activate: conda activate yolov12"

git clone https://github.com/sunsmarterjie/yolov12 

wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.3/flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl 

cd yolov12

pip install -r requirements.txt

pip install -e .
