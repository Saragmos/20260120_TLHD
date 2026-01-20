import warnings, os
warnings.filterwarnings('ignore')
from ultralytics import YOLO

import torch.distributed

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/11/ours.yaml') 
    model.train(data='/home/cug615/myProject/datasets/Dut-Anti-UAV/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300, 
                batch=16,
                close_mosaic=10,
                workers=8,
                device='0, 1',
                optimizer='SGD',
                # patience=100, # set 0 to close earlystop. 30
                # project='runs/Det-Fly',
                # project='runs/AntiUAV410',
                # seed=42,
                project='runs/Dut-anti-UAV',
                name='yolo11',
                )