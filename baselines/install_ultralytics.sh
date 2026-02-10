
echo "Create & activate ultralytics environment before installation"

echo "conda create -n ultralytics  python=3.10 -y"

pip install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=11.8 -c pytorch -c nvidia

git clone https://github.com/ultralytics/ultralytics 

cd ultralytics 

pip install -e .

pip install tensorboard

echo "DONE: ultralytics is installed"