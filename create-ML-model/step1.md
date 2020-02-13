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

`import tensorflow as tf`{{execute}}
`import numpy as np`{{execute}}
`import math`{{execute}}
`import matplotlib.pyplot as plt`{{execute}}
`import matplotlib.animation as animation`{{execute}}
`sess = tf.Session()`{{execute}}
`hello = tf.constant("Hello from tensorflow")`{{execute}}

Data:

`num_mq_data = 160`{{execute}}
`np.random.seed(42)`{{execute}}
`mq_data_size = np.random.randint(low=1000, high=3500, size=num_mq_data)`{{execute}}
`np.random.seed(42)`{{execute}}
`mq_data_failure = mq_data_size * 100.0 + np.random.randint(low=20000, high=70000, size=num_mq_data)`{{execute}}

 