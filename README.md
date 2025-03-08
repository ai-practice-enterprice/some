
## To create an image  (choose your own name or not)
docker build -t some .

## To run a container from the created image 
docker run -it -p 5002:5002 -p 5003:5003 -p 5004:5004 --name somecontainer some 

## After runnning the container, just send a get request to localhost:5004
