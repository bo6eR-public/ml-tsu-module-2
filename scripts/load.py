from roboflow import Roboflow
rf = Roboflow(api_key="beJvZ6246OssSRS6Weat")
project = rf.workspace("s-workspace-mcr92").project("my-first-project-lj0to")
version = project.version(2)
dataset = version.download("yolov8")