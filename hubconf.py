dependencies = ['torch']
import torch

# Ultralytics yolov5n
def yolov5n(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=pretrained)
    return model

# Ultralytics yolov5s
def yolov5s(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=pretrained)
    return model

# Ultralytics yolov5m
def yolov5m(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=pretrained)
    return model

# Ultralytics yolov5l
def yolov5l(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=pretrained)
    return model

# Ultralytics yolov5x
def yolov5x(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=pretrained)
    return model