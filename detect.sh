#!/bin/bash

python detect.py --source inference/helmet-vid-frames --cfg cfg/yolor_p6.cfg --weights  runs/train/coco-helmet/weights/best.pt --conf 0.25 --img-size 1280 --device cpu --output inference/helmet-vid-results --names data/helmet.names --classes 0