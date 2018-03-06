#!/bin/sh
sudo docker stop $(docker ps -aq)
sudo docker rm $(docker ps -aq)
sudo docker build -t jobchain-site .
sudo docker run -p 8080:80 -it --name jchain-site jobchain-site
