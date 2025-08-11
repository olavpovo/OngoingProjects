#!/bin/bash

# Sync Big Brother Canada

rsync -azhP ~/Downloads/tv/Big\ Brother\ Canada/ olav@192.168.1.106:/mnt/media/tv/Big\ Brother\ Canada/


# Sync Survivor

rsync -azhP ~/Downloads/tv/Survivor/ olav@192.168.1.106:/mnt/media/tv/Survivor/


# Sync Naked and Afraid

rsync -azhP ~/Downloads/tv/Naked\ and\ Afraid/ olav@192.168.1.106:/mnt/media/tv/Naked\ and\ Afraid/


echo "Rsync Done!"
