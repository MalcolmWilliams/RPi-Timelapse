#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner -d /dev/video0 /home/pi/webcam/$DATE.jpg
cp /home/pi/webcam/$DATE.jpg /home/pi/server/img_latest.jpg
