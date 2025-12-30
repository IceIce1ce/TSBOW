# usage: bash filename.sh

DATA_PATH='NGOCHDM/Dataset/'
DATA_NAME='TSBOW'

MODEL_PATH='yolov12/runs/detect/'

CUDA_DEVICE='cuda:1'
IMAGE_SIZE=1280 
CONF_SCORE=0.5
IOU_DETECT=0.6
SPLIT_PATH='test'
MAX_DETECT=300

BATCH_SIZE_YOLOv8x=128
BATCH_SIZE_YOLO11x=64
BATCH_SIZE_YOLO12x=56
BATCH_SIZE_RTDETRl=14

# remove cache file
# rm "${DATA_PATH}${DATA_NAME}/test/labels.cache"

##############################

classification="SCENARIO WEATHER SCALE ROADTYPE TRAFFIC"
class_sn_value="road intersection specialcase disaster"
class_w_value="normal haze rain snow"
class_s_value="fine medium coarse"
class_r_value="urban standard boulevard"
class_t_value="light moderate heavy"

VERSION_NAME="TSBOWv01"

##############################

# scenario
CUDA_DEVICE='cuda:2'

for scenario in $class_sn_value
do
    python validation_YOLO.py \
        -d $DATA_PATH   -n $DATA_NAME   -y "${VERSION_NAME}_SCENARIO_${scenario}"   \
        -p $MODEL_PATH  -m "ABLATION/yolov12x_TSBOW"                                \
        -c $CUDA_DEVICE -i $IMAGE_SIZE  -b $BATCH_SIZE_YOLO12x                      \
        --conf $CONF_SCORE      --iou $IOU_DETECT    --split $SPLIT_PATH            \
        --max_det $MAX_DETECT   --task "ablation"
done


## weather
CUDA_DEVICE='cuda:1'

for weather in $class_w_value
do
    python validation_YOLO.py \
        -d $DATA_PATH   -n $DATA_NAME   -y "${VERSION_NAME}_WEATHER_${weather}"     \
        -p $MODEL_PATH  -m "ABLATION/yolov12x_TSBOW"                                \
        -c $CUDA_DEVICE -i $IMAGE_SIZE  -b $BATCH_SIZE_YOLO12x                      \
        --conf $CONF_SCORE  --iou $IOU_DETECT    --split $SPLIT_PATH                \
        --max_det $MAX_DETECT   --task "ablation"
done


## scale
CUDA_DEVICE='cuda:2'

for scale in $class_s_value
do
    python validation_YOLO.py \
        -d $DATA_PATH   -n $DATA_NAME   -y "${VERSION_NAME}_SCALE_${scale}"         \
        -p $MODEL_PATH  -m "ABLATION/yolov12x_TSBOW"                                \
        -c $CUDA_DEVICE -i $IMAGE_SIZE  -b $BATCH_SIZE_YOLO12x                      \
        --conf $CONF_SCORE  --iou $IOU_DETECT    --split $SPLIT_PATH                \
        --max_det $MAX_DETECT   --task "ablation"
done


## roadtype
CUDA_DEVICE='cuda:3'

for roadtype in $class_r_value
do
    python validation_YOLO.py \
        -d $DATA_PATH   -n $DATA_NAME   -y "${VERSION_NAME}_ROADTYPE_${roadtype}"   \
        -p $MODEL_PATH  -m "ABLATION/yolov12x_TSBOW"                                \
        -c $CUDA_DEVICE -i $IMAGE_SIZE  -b $BATCH_SIZE_YOLO12x                      \
        --conf $CONF_SCORE  --iou $IOU_DETECT    --split $SPLIT_PATH                \
        --max_det $MAX_DETECT   --task "ablation"
done


## traffic
CUDA_DEVICE='cuda:1'

for traffic in $class_t_value
do
    python validation_YOLO.py \
        -d $DATA_PATH   -n $DATA_NAME   -y "${VERSION_NAME}_TRAFFIC_${traffic}"     \
        -p $MODEL_PATH  -m "ABLATION/yolov12x_TSBOW"                                \
        -c $CUDA_DEVICE -i $IMAGE_SIZE  -b $BATCH_SIZE_YOLO12x                      \
        --conf $CONF_SCORE  --iou $IOU_DETECT    --split $SPLIT_PATH                \
        --max_det $MAX_DETECT   --task "ablation"
done