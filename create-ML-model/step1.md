The first phase in ML Development is 
DATA

![ML Integration Flow](/laura-schornack/scenarios/set-up/assets/data.png)

Collecting and transforming data usually takes 70% of the time of your project.  

For the purposes of this scenario, we will generate our data with a python random number generator.  
The numbers that we generate will range from 1000 to 3500 and will contain 160 datapoints.  

Before we get started, run these "quick setup" steps.  For the details on these steps, go back to "Scenario 1: Environment Setup" of this tutorial.  

Quick Setup:
`git clone https://github.com/lauraschornack/katacoda1.git`{{execute}}

`cd katacoda1/create-ML-model`{{execute}}

`docker build . -t katacoda1docker`{{execute}}

docker run -p 8500:8500 -it --rm katacoda1docker
`docker run katacoda1docker`{{execute}}

`python3 hello-data.py`{{open}}

`python3 hello-data.py`{{execute}}


