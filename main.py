from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(data="new.yaml", epochs=1, imgsz=640)
