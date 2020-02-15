import tensorflow as tf
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hey, we have Flask in a Docker container!'

#if __name__ == '__main__':
#    app.run(port=8500)

sess = tf.Session()
hello = tf.constant("Hello Laura from TensorFlow")
print(sess.run(hello))
a = tf.constant(20)
b = tf.constant(22)
print('a + B = {0}'.format(sess.run(a+b)))
num_mq_data = 160
np.random.seed(42)
mq_data_size = np.random.randint(low=1000, high=3500, size=num_mq_data)
np.random.seed(42)
mq_data_failure = mq_data_size * 100.0 + np.random.randint(low=20000, high=70000, size=num_mq_data)
#plt.plot(mq_data_size, mq_data_failure, "bx")
#plt.ylabel("Failure")
#plt.xlabel("MQ_VAR")
#plt.show()

print(mq_data_size)

#

#Normalize values to prevent under/overflow
def normalize(array):
    return (array - array.mean()) / array.std()

#Take the first 70% of your data as training samples
num_train_samples = math.floor(num_mq_data * .7)

#Define Training Data
train_mq_data_size = np.asarray(mq_data_size[:num_train_samples])
train_failure = np.asanyarray(mq_data_failure[:num_train_samples:])

train_mq_data_size_norm = normalize(train_mq_data_size)
train_failure_norm = normalize(train_failure)

#Define Test Data
test_mq_data_size = np.asarray(mq_data_size[:num_train_samples])
test_mq_data_failure = np.asanyarray(mq_data_failure[:num_train_samples:])
test_mq_data_size_norm = normalize(train_mq_data_size)
test_failure_norm = normalize(train_failure)

# - End of Data
