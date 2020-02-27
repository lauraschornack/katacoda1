Before we get started, run these "quick setup" steps.  For the details on these steps,go back to "Scenario 1: Environment Setup" of this tutorial, where we went over building a simple docker image in detail.    

We will start by building our environment, using our Dockerfile from the Scenario 1.

Step:
Click on the link below to open the Dockerfile.  
`Dockerfile`{{open}}

Step:
Build the docker file to put the following components into our container.
`docker build . -t katacoda1docker`{{execute}}

Step:
Run the docker container:
`docker run -p 8500:8500 -it --rm katacoda1docker /bin/bash`{{execute}}
