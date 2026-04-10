from ultralytics import YOLO

model = YOLO("../runs/detect/train/weights/best.pt")
model.val(data="data/data.yaml")

# model.predict(source="sources/video.mp4", show=True)
# model.predict(source=0, show=True)

