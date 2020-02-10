This scenario will take us through the steps we need to set up our tensorflow and python environment to create a basic ML model.
If you choose to do containers, go with Option 1.
If you chose to do a setup without containers, skip down to Option 2.  
You do not need both options.  

Option 1: Setup with containers:

For each step, either click on the highlighted text to run it in the terminal, or if you prefer, you can type it.  

Step 1:
Pull down docker file from my git hub
`git clone https://github.com/lauraschornack/katacoda1.git`{{execute}}

Step 2:
`cd katacoda1/set-up`{{execute}}

Step 3:
`docker build . -t katacoda1docker`{{execute}}

Step 4:
`docker run -p 8500:8500 -it --rm katacoda1docker`{{execute}}


Render port 8500: https://[[HOST_SUBDOMAIN]]-8500-[[KATACODA_HOST]].environments.katacoda.com/

Render port 80: https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com/

Display page allowing user to select port:
https://[[HOST_SUBDOMAIN]]-[[KATACODA_HOST]].environments.katacoda.com/
        
---------------
Option 2: Setup without containers

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

Step 7:
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

----
A Katacoda scenario is a series of Markdown files, bash scripts and a JSON file to define how your scenario should be configured, the text for the scenario and any automation required.

## Task

Clone our example repository that contains the set of documentation with the following command:

`git clone https://github.com/katacoda/scenario-examples.git katacoda-scenario-examples`{{execute}}

Within the repository, you will see a set of examples of implementing various Katacoda functionality.

The scenario you are currently reading is in the directory `ls -lha katacoda-scenario-examples/create-scenario-101`{{execute}}. The directory name is what defines the URL.

An example of the current step is `katacoda-scenario-examples/create-scenario-101/step1.md`{{open}}

All the steps are collected via a JSON file, for example, `katacoda-scenario-examples/create-scenario-101/index.json`{{open}}.

The JSON file defines the scenario title, the description, steps order, the UI layout and environment. You can find more about the layouts within our scenarios at [katacoda.com/docs/scenarios/layouts](https://katacoda.com/docs/scenarios/layouts) and environments at [katacoda.com/docs/scenarios/environments](https://katacoda.com/docs/scenarios/environments).

