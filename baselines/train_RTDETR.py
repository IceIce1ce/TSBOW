from argparse import ArgumentParser

from ultralytics import RTDETR

def training(args):
    model_name = args.model + '.pt'
    model = RTDETR(model_name)
    model.info()

    data_path = args.path2data
    data_name = args.name
    data_yaml = f"{data_path + data_name}/{data_name}.yaml"

    results = model.train(data=data_yaml,         device=args.device_cuda, 
                          imgsz=args.image_size,  batch=args.batch_size,
                          epochs=args.epochs,     cache=args.cache,
                          name=f"{args.model}_{data_name}")
    
    return results

def parse_args():
    parser = ArgumentParser("Train RT-DETR models")

    # MODEL RELATED
    parser.add_argument('-m', '--model',        type=str,
                        default="rtdetr-l", 
                        help='Choose model name for -m or --model: rtdetr-l or rtdetr-x')
    parser.add_argument('-c', '--device_cuda',  type=str, 
                        default='cuda:0', 
                        help='Choose cuda device for -c or --device-cuda: cuda:0 or [0, 1, 2]')
    parser.add_argument('-e', '--epochs',       type=int,
                        default=40,
                        help='Enter number of training epochs for -e or --epochs')
    parser.add_argument('-i', '--image_size',   type=int,
                        default=1280,
                        help='Enter image size for -i or --image_size')
    parser.add_argument('-b', '--batch_size',   type=int,
                        default=16,
                        help='Enter batch size for -b or --batch_size')
    parser.add_argument('--cache',   type=bool,
                        default=False,
                        help='Cache: True or False')
    
    # DATA RELATED
    # Full path to dataset: /media/hdmngoc/ssd_02/DataCreation/TSBOW/TSBOW.yaml
    parser.add_argument('-d', '--path2data',    type=str, 
                        default='/media/hdmngoc/ssd_02/DataCreation/', 
                        help='Enter the path of data.')
    parser.add_argument('-n', '--name',         type=str,   
                        default="TSBOW", 
                        help='Enter name of YAML file: TSBOW')
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args    = parse_args()
    results = training(args=args)