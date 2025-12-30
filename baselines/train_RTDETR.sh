
DATA_PATH='NGOCHDM/Dataset/'
DATA_NAME='TSBOW'

# Choose model version: 'rtdetr-l', 'rtdetr-x'
MODEL_VER='rtdetr-x'

CUDA_DEVICE='[0,1,2,3]'
EPOCH_TRAIN=100
BATCH_SIZE=36
IMAGE_SIZE=1280

export NCCL_IB_GID_INDEX=3
export NCCL_P2P_DISABLE=1

python train_RTDETR.py \
    -d $DATA_PATH   -n $DATA_NAME \
    -m $MODEL_VER   -c $CUDA_DEVICE \
    -e $EPOCH_TRAIN -b $BATCH_SIZE \
    -i $IMAGE_SIZE
