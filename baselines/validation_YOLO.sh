
DATA_PATH='NGOCHDM/Dataset/'
DATA_NAME='TSBOW'

###############
# ultralytics
### yolov8x
# MODEL_PATH='/media/vsw/SSD_1/NGOCHDM/SourceCode/ultralytics/runs/detect/' 
# MODEL_NAME='yolov8x'
# BATCH_SIZE=128

### yolov11x
# MODEL_PATH='/media/vsw/SSD_1/NGOCHDM/SourceCode/ultralytics/runs/detect/' 
# MODEL_NAME='yolo11x'
# BATCH_SIZE=64

### yolov12
MODEL_PATH='/media/vsw/SSD_1/NGOCHDM/SourceCode/yolov12/runs/detect/' 
MODEL_NAME='yolov12x'
BATCH_SIZE=56

### rtdetr-x
# MODEL_PATH='/media/vsw/SSD_1/NGOCHDM/SourceCode/ultralytics/runs/detect/' 
# MODEL_NAME='rtdetr-x'
# BATCH_SIZE=14
###############

CUDA_DEVICE='cuda:2'
IMAGE_SIZE='960 1120 1280 1440 1600'
CONF_SCORE=0.5
IOU_DETECT=0.6
SPLIT_PATH='test'
MAX_DETECT=300


for imgsize in $IMAGE_SIZE
do
    CUDA_VISIBLE_DEVICES='2' \
    python validation_YOLO.py \
        -d $DATA_PATH       -n $DATA_NAME \
        -p $MODEL_PATH      -m "${MODEL_NAME}_${DATA_NAME}" -c $CUDA_DEVICE \
        -i $imgsize         -b $BATCH_SIZE                  --conf $CONF_SCORE  \
        --iou $IOU_DETECT   --split $SPLIT_PATH             --max_det $MAX_DETECT \
        -r "EVALUATION/${MODEL_NAME}_${imgsize}"
done

# CUDA_VISIBLE_DEVICES='1' \
# python validation_YOLO.py \
#     -d $DATA_PATH   -n $DATA_NAME \
#     -p $MODEL_PATH  -m $"yolo11x.pt" \
#     -c $CUDA_DEVICE -i $IMAGE_SIZE  -b 10  --conf $CONF_SCORE  \
#     --iou $IOU_DETECT    --split $SPLIT_PATH    --max_det $MAX_DETECT
