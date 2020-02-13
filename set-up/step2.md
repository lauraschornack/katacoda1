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




