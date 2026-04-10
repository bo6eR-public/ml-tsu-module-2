# ml-tsu-module-2
by Timur Nikulin, 972403

## Work steps
1. Load own dataset or use `scripts/load.py` to load ready dataset with license plates (rename downloaded folder to `data`)
2. Train your model (use `scripts/train.py`). You have to have `data` folder with `data.yaml` into one (check this one)
3. Check your model that is working or not with `scripts/check.py`
4. Move `runs/detect/train/weight/best.pt` to `project/weights`
5. Run `model.py` to start analysis your custom video or web-camera\
   `py project/main.py --mode video --source sources/video.mp4` - for your video\
   `py project/main.py --mode camera` - for your web-camera
6. If you want to run docker:\
   `docker-compose up video` - to run with video source\
   `docker-compose up camera` - to run with live camera source

## Information sources
`dataset (video) for roboflow was taken from` - [shutterstock](https://www.shutterstock.com/ru/video/search/car-plates-russia)\
`info abot yolo work` - [habr article](https://habr.com/ru/articles/821971/)\
`yolo docs` - [docs.ultralytics.com](https://docs.ultralytics.com/)\
`sources/video.mp4` - [source video for check](https://www.pexels.com/video/busy-highway-traffic-at-sunset-31779728/)