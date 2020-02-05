This scenario will take us through the steps we need to set up our tensorflow and python environment to create a basic ML model.

Install python.
`sudo add-apt-repository ppa:myhome/python3.6`

`sudo apt-get update`{{execute}}

`sudo apt-get install python3`{{execute}}

Install tensorflow.
`pip install tensorflow==1.2.0 --ignore-installed`{{execute}}

Open a python shell with python3
`python3`{{execute}}

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

