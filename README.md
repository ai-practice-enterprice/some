
## To create an image 
docker build -t some .

## To run a container from the created image
docker run -it -p 5002:5002 -p 5003:5003 -p 5004:5004 --name somecontainer some 
