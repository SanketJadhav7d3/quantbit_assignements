
from ultralytics import YOLO
import cv2
import argparse

parser = argparse.ArgumentParser(description="YOLO object detection")

parser.add_argument("--model", type=str, required=False, default="yolo11n.pt", help="YOLO model path")
parser.add_argument("--video", type=str, required=True, help="Video path")

args = parser.parse_args()

model = YOLO(args.model)

results = model.track(source=args.video, show=True)  

