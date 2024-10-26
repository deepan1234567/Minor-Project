from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.predict(source="C:/Users/LENOVO/OneDrive/Desktop/Minor Project/new/train/images/02fe72bf-R_1200_jpg.rf.b8ae13212e1ed803d955269bceca7a15.jpg",show=True,save=True)
