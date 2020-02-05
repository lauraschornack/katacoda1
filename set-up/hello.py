import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
sess = tf.Session()
hello = tf.comstant("Hello Laura from TensorFlow")
print (sess.run(hello))
a = tf.constant(20)
b = tf.constant(22)
print('a+B={0}'.format(sess.run(a+b)))

