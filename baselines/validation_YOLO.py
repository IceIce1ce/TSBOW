from argparse import ArgumentParser
# from pathlib import Path

from ultralytics import YOLO
from ultralytics import RTDETR


def validation(args):
    model_path = args.path2model
    model_file = args.model
    model_pt_file = model_path + model_file + "/weights/best.pt"
    if "rtdetr" in model_file:
        model = RTDETR(model_pt_file)
    else:
        model = YOLO(model_pt_file)
    
    data_path = args.path2data
    data_name = args.name
    data_yaml = f"{data_path + data_name}/{data_name}.yaml"

    results_name = args.results_name

    results = model.val(data=data_yaml,         device=args.device_cuda, 
                        imgsz=args.image_size,  batch=args.batch_size,
                        conf=args.conf,         iou=args.iou,
                        split=args.split,       max_det=args.max_det,
                        name=f"EVALUATION/{model_file}_evaluation", save_json=True)
    
    return results


def validation_ablation(args):
    model_path = args.path2model
    model_file = args.model
    model_pt_file = model_path + model_file + "/weights/best.pt"
    if "rtdetr" in model_file:
        model = RTDETR(model_pt_file)
    else:
        model = YOLO(model_pt_file)
    
    data_path = args.path2data
    data_name = args.name
    data_yaml = args.yaml
    yaml_path = f"{data_path + data_name}/{data_yaml}.yaml"

    results_name = args.results_name

    results = model.val(data=yaml_path,         device=args.device_cuda, 
                        imgsz=args.image_size,  batch=args.batch_size,
                        conf=args.conf,         iou=args.iou,
                        split=args.split,       max_det=args.max_det,
                        name=f"ABLATION/{model_file}_evaluation", save_json=True)
    
    print(f"\n\nEVALUATION\n   data_yaml: {data_yaml}\n")

    return results
    

def validation_comparison(args):
    model_path = args.path2model
    model_file = args.model
    if "_" not in model_file:
        model_pt_file = f"{model_file}.pt"
    else:
        model_pt_file = model_path + model_file + "/weights/best.pt"
    if "rtdetr" in model_file:
        model = RTDETR(model_pt_file)
    else:
        model = YOLO(model_pt_file)
    
    data_path = args.path2data
    data_name = args.name
    data_yaml = f"{data_path + data_name}/{data_name}.yaml"

    results_name = args.results_name

    conf_name = int(args.conf * 10)

    results = model.val(data=data_yaml,         device=args.device_cuda, 
                        imgsz=args.image_size,  batch=args.batch_size,
                        conf=args.conf,         iou=args.iou,
                        split=args.split,       max_det=args.max_det,
                        name=f"COMPARISON/{model_file}_evaluation_conf{conf_name:02d}", save_json=True)


def visualize_():
    print()


def parse_args():
    parser = ArgumentParser()

    # MODEL RELATED
    parser.add_argument('-p', '--path2model',   type=str,  
                        default='/media/ngochdm/Projects/__SERVER_05__/SourceCode/ultralytics/runs/detect/', 
                        help='Enter the path of detection model for -p or --path2model')
    parser.add_argument('-m', '--model',        type=str,
                        default="yolo11x", 
                        help='Choose model name for -m or --model: yolov8x or yolo11x')
    parser.add_argument('-c', '--device_cuda',  type=str, 
                        default='cuda:0', 
                        help='Choose cuda device for -c or --device-cuda: cuda:0 or [0, 1, 2]')
    parser.add_argument('-r', '--results_name',  type=str, 
                        help='Choose results folder name for -r or --results_name')
    
    parser.add_argument('-i', '--image_size',   type=int,
                        default=640,
                        help='Enter image size for -i or --image_size')
    parser.add_argument('-b', '--batch_size',   type=int,
                        default=16,
                        help='Enter batch size for -b or --batch_size')
    
    parser.add_argument('--conf',   type=float, default=0.001,
                        help='Enter confidence score for --conf')
    parser.add_argument('--iou',    type=float, default=0.6,
                        help='Enter IoU for --iou')
    parser.add_argument('--split',  type=str,   default='test',
                        help='Choose dataset split to evaludate --split: train or val or test')
    parser.add_argument('--max_det',type=int,   default=300,
                        help='Enter maximum number of detections for --max_det')
    
    parser.add_argument('--task',  type=str,   default='',
                        help='Choose task to evaluate --task: <none> or comparison or ablation')
    
    # DATA RELATED
    parser.add_argument('-d', '--path2data',    type=str, 
                        default='/media/hdmngoc/ssd_02/DataCreation/', 
                        help='Enter the path of data.')
    parser.add_argument('-n', '--name',         type=str,   
                        default="SUWON_DATASET_VER01_GT", 
                        help='Enter name of YAML file')
    parser.add_argument('-y', '--yaml',         type=str,   
                        default="SUWON_DATASET_VER01_GT", 
                        help='Enter name of YAML file')
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args    = parse_args()
    if args.task == "comparison":
        results = validation_comparison(args=args)
    elif args.task == "ablation":
        results = validation_ablation(args=args)
    else:    
        results = validation(args=args)