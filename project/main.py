import argparse
import cv2
import time
import logging
from model_impl import My_LicensePlate_Model

logging.basicConfig(
    filename='./data/log_file.log',
    level=logging.INFO
)

model = My_LicensePlate_Model()

# This function provides the processing the video (works on each frame in accordance with the best model best.pt)
def process_video(source):
    cap = cv2.VideoCapture(source)

    while cap.isOpened():
        try:
            ret, frame = cap.read()
            if not ret:
                break

            start = time.time()
            detections = model.detect_plates(frame)

            latency = time.time() - start
            logging.info(f"Latency: {latency}")

            for d in detections:
                x1, y1, x2, y2 = map(int, d["bbox"])
                cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)

            cv2.imshow("frame", frame)
            if cv2.waitKey(1) == 27:
                break
        except Exception as er:
            logging.error(er)

# The source is web-camera
def process_camera():
    process_video(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["video", "camera"])
    parser.add_argument("--source", default="sources/video.mp4")

    args = parser.parse_args()

    if args.mode == "video":
        process_video(args.source)
    else:
        process_camera()