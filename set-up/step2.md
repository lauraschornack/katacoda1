Setup without containers

Step 1:
Install python.
`sudo add-apt-repository ppa:myhome/python3.6`

Step 2:
`sudo apt-get update`{{execute}}

Step 3:
`sudo apt-get install python3`{{execute}}

Step 4:
Install tensorflow.
`pip install tensorflow==1.2.0 --ignore-installed`{{execute}}

Step 5:
Install tensorflow.
`pip install matplotlib`{{execute}}

Step 6:
Open a python shell with python3
`python3`{{execute}}

Test your environment:
Test your tensorflow install by running the following import commands.
`import tensorflow as tf`{{execute}}

`import numpy as np`{{execute}}

`import math`{{execute}}

`import matplotlib.pyplot as plt`{{execute}}

`import matplotlib.animation as animation`{{execute}}

`sess = tf.Session()`{{execute}}

`hello = tf.constant("Hello from tensorflow")`{{execute}}

`print(sess.run(hello))`{{execute}}

`a = tf.constant(20)`{{execute}}

`b = tf.constant(22)`{{execute}}

`print('a + B = {0}'.format(sess.run(a+b)))`{{execute}}




Option 1: Setup with containers:

For each step, either click on the highlighted text to run it in the terminal, or if you prefer, you can type it.  

Container Setup:

Step 1:
Pull down docker file from my git hub
`git clone https://github.com/lauraschornack/katacoda1.git`{{execute}}

Step 2:
`cd katacoda1/set-up`{{execute}}

The Docker file looks like this:
We are adding the following components into our container.
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