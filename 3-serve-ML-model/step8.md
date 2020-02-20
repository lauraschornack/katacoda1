Run the docker file, which will create an entry point for flask.
Build the docker file. 
`docker build . -t katacoda1docker`{{execute}}

Step:
`docker run -p 8500:8500 -it --rm katacoda1docker`{{execute}}