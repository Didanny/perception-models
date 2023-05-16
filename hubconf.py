dependencies = ['torch']
import torch

# Ultralytics yolov5n
def yolov5n(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=pretrained, **kwargs)
    return model

# Ultralytics yolov5s
def yolov5s(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=pretrained, **kwargs)
    return model

# Ultralytics yolov5m
def yolov5m(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=pretrained, **kwargs)
    return model

# Ultralytics yolov5l
def yolov5l(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=pretrained, **kwargs)
    return model

# Ultralytics yolov5x
def yolov5x(pretrained=False, **kwargs):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=pretrained, **kwargs)
    return model

# WongKinYiu yolov7
#model_path='/home/ljk/models/yolov7.pt'
#def yolov7(pretrained=True, **kwargs):
#    model = torch.hub.load("WongKinYiu/yolov7", "custom", model_path, pretrained=pretrained, **kwargs)
#    return model


# WongKinYiu yolov7
#def yolov7(pretrained=False, **kwargs):
 #   model = torch.hub.load('WongKinYiu/yolov7', 'yolov7', pretrained=pretrained, **kwargs)
 #   return model


# WongKinYiu yolov7
model_path='/home/ljk/perception-model-pruning/exact_models/yolov7.pt'
def yolov7(pretrained=False, **kwargs):
    model = torch.hub.load("WongKinYiu/yolov7", "custom", model_path, pretrained=pretrained, **kwargs)
    return model
