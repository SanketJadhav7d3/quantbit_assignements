

from roboflow import Roboflow

rf = Roboflow(api_key="your api key ")
project = rf.workspace("fire-rqbio").project("fire-and-smoke-yikzn")
version = project.version(3)
dataset = version.download("yolov9")

