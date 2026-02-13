
echo "Create & activate Xanylabeling environment before installation"

echo "     create: conda create -n Xanylabeling  python=3.9 -y"

echo "     activate: conda activate Xanylabeling"

# Install ONNX Runtime GPU (CUDA 12.x)
pip install onnxruntime-gpu --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-12/pypi/simple/ 

# Download the source code
git clone https://github.com/CVHub520/X-AnyLabeling.git
cd X-AnyLabeling/

# Install Dependencies
pip install -U pip
pip install -r requirements-dev.txt
