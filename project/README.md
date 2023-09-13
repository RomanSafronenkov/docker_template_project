# Docker packing

To run this code as a docker container you should have docker installed
1) Build the image from the ```/docker_template_project/project/``` path 
```shell
sudo docker build -t flask_project . 
```
2) Check the images and look at created image
```shell
sudo docker images
```
3) Once it is built you can run it (-d: detach mode, -p: HOST_PORT:CONTAINER_PORT, --name: container name)
```shell
sudo docker run -d -p 8080:8080 --name=proj flask_project
```
4) Check running container:
```shell
sudo docker ps
```
5) Try to send JSON to it, using ```/docker_template_project/tests/curl_test```
```shell
bash curl_test
```
All we need!

If you need to stop and remove container and created image run this:
```shell
sudo docker rm -f proj && sudo docker rmi flask_project
```