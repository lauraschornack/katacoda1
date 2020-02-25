Before we get started, run these "quick setup" steps.  For the details on these steps,go back to "Scenario 1: Environment Setup" of this tutorial, where we went over building a simple docker image in detail.    

We will start by using our Dockerfile from the Scenario 1.
(Note - this docker file will be changed later)

Step:
`cd ..`{{execute}}

Step
`Dockerfile`{{open}}

Step:
comment out the last two lines



Step:
`sudo apt-get update`{{execute}}

Step:
Install tensorflow.
`pip install tensorflow==1.2.0 --ignore-installed`{{execute}}






The Docker file looks like this:
We are addipen the code before flask has been added

The Docker file looks like this:
We are adding the following components into our container.
`hello-pre-flask.py`{{open}}.
ng the following components into our container.
`katacoda1docker`{{open}}.

Step 3:
Build the docker file. 
`docker build . -t katacoda1docker`{{execute}}

Step 4:
`docker run -p 8500:8500 -it --rm katacoda1docker`{{execute}}


Render port 8500: https://[[HOST_SUBDOMAIN]]-8500-[[KATACODA_HOST]].environments.katacoda.com/

Render port 80: https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com/

Display page allowing user to select port:
https://[[HOST_SUBDOMAIN]]-[[KATACODA_HOST]].environments.katacoda.com/