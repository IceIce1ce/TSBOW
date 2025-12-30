
DATA_PATH='NGOCHDM/Dataset/'
DATA_NAME='TSBOW'

# Model_ver can be: yolov8, yolo11, yolov12
# Weights can be: n, s, m, l, x
MODEL_VER='yolov12x'        

CUDA_DEVICE='[0,1,2,3]'
EPOCH_TRAIN=100
BATCH_SIZE=40
IMAGE_SIZE=1280
CACHE=True

TRAIN_STATE='start'

export NCCL_IB_GID_INDEX=3
export NCCL_P2P_DISABLE=1

python train_YOLO.py \
    -d $DATA_PATH   -n $DATA_NAME \
    -m $MODEL_VER   -c $CUDA_DEVICE \
    -e $EPOCH_TRAIN -b $BATCH_SIZE \
    -i $IMAGE_SIZE  --cache $CACHE \
    --state $TRAIN_STATE
