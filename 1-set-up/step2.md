The set-up for this type of environment would have looked like this:

Setup without containers

Step:
`sudo apt-get update`{{execute}}

Step:
Install tensorflow.
`pip install tensorflow==1.2.0 --ignore-installed`{{execute}}

Step:
Install matplotlib.
`pip install matplotlib`{{execute}}

Step:
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




