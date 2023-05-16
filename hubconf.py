dependencies = ['torch']
import torch
import os

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


# # WongKinYiu yolov7
# def yolov7(pretrained=False, **kwargs):
#     model = torch.hub.load('WongKinYiu/yolov7', 'yolov7', pretrained=pretrained, **kwargs,force_reload=True)
#     return model


# # WongKinYiu yolov7
# model_path='/home/ljk/perception-model-pruning/exact_models/yolov7.pt'
# def yolov7(pretrained=False, **kwargs):
#     model = torch.hub.load("WongKinYiu/yolov7", "custom", model_path, pretrained=pretrained, **kwargs)
#     return model

# WongKinYiu yolov7
def yolov7(pretrained=False, **kwargs):
    model_path='/home/ljk/perception-model-pruning/exact_models/yolov7.pt'
    if not os.path.exists(model_path):
       print
       os.system(
          f"wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/{os.path.basename(model_path)} -O {model_path}"
       )

    # load model
    try:
        model = torch.hub.load("WongKinYiu/yolov7", "custom", model_path)
    except:
        raise Exception("Failed to load model from {}".format(model_path))
    return model
