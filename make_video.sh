#!/bin/bash
scp pi@192.168.0.42:~/webcam/* ./imgs_raw/
ssh pi@192.168.0.42 "mv ~/webcam/* ~/webcam_bk/"
python filter_img.py
mv ./imgs_raw/* ./imgs_bk/
ffmpeg -y -r 60 -pattern_type glob -i './imgs_filt/*.jpg' -c:v mjpeg -q:v 5 output.avi
mv output.avi /mnt/c/Users/malcolm/Desktop/
