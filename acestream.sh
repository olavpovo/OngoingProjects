#!/bin/bash

echo "What channel would you like to watch??"
read channel

#if [channel = "cric"]
#then
#$channel = 6d95e4b0893e155cc674b84e0763150c445d3ddd

/Users/olav/Docker/mac/docker-acestream-server/playstream.py \
--ace-stream-pid $channel \
--player /Applications/VLC.app/Contents/MacOS/vlc