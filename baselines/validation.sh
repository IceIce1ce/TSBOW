
###########################################################################
# INSTRUCTIONS
# Select model to validate: yolov8x, yolov11x, yolov12x, rtdetr-x
# Uncomment the corresponding block and set BATCH_SIZE accordingly
###########################################################################
### yolov8x
# MODEL_PATH='ultralytics/runs/detect/' 
# MODEL_NAME='yolov8x'
# BATCH_SIZE=128

### yolo11x
# MODEL_PATH='ultralytics/runs/detect/' 
# MODEL_NAME='yolo11x'
# BATCH_SIZE=64

### yolov12x
MODEL_PATH='yolov12/runs/detect/' 
MODEL_NAME='yolov12x'
BATCH_SIZE=56

### rtdetr-x
# MODEL_PATH='ultralytics/runs/detect/' 
# MODEL_NAME='rtdetr-x'
# BATCH_SIZE=14
###########################################################################

# Dataset configuration
DATA_PATH='NGOCHDM/Dataset/'
DATA_NAME='TSBOW'

# Validation configuration
CUDA_DEVICE='cuda:2'
IMAGE_SIZE='960 1120 1280 1440 1600'
CONF_SCORE=0.5
IOU_DETECT=0.6
SPLIT_PATH='test'
MAX_DETECT=300


# Validation with different image sizes

for imgsize in $IMAGE_SIZE
do
    CUDA_VISIBLE_DEVICES='2' \
    python validation.py \
        -d $DATA_PATH       -n $DATA_NAME \
        -p $MODEL_PATH      -m "${MODEL_NAME}_${DATA_NAME}" -c $CUDA_DEVICE \
        -i $imgsize         -b $BATCH_SIZE                  --conf $CONF_SCORE  \
        --iou $IOU_DETECT   --split $SPLIT_PATH             --max_det $MAX_DETECT \
        -r "EVALUATION/${MODEL_NAME}_${imgsize}"
done


# Validation with fixed image size

# CUDA_VISIBLE_DEVICES='1' \
# python validation.py \
#     -d $DATA_PATH   -n $DATA_NAME \
#     -p $MODEL_PATH  -m $"yolo11x.pt" \
#     -c $CUDA_DEVICE -i $IMAGE_SIZE  -b 10  --conf $CONF_SCORE  \
#     --iou $IOU_DETECT    --split $SPLIT_PATH    --max_det $MAX_DETECT
