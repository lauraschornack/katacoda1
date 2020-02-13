import tensorflow as tf
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



import matplotlib.animation as animation
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

if __name__ == '__main__':
    app.run(port=8500)

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
    plt.plot(mq_data_size, mq_data_failure, "bx")
    plt.ylabel("Failure")
    plt.xlabel("MQ_VAR")
    plt.show()

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

    #Define tensor place holders to pass data into the graph - to descend down the gradient
    tf_mq_data_size = tf.placeholder("float", name="mq_data_size")
    tf_failure = tf.placeholder("float", name="failure")

    #Define the variables holding the VALUES TO BE TRAINED size factor and failure we set during training.
    #We initialize them to some random values based on the normal distribution
    tf_size_factor = tf.Variable(np.random.randn(), name="size_factor")
    tf_failure_offset = tf.Variable(np.random.randn(), name="failure")

    #

    # 2. Define the operations for the predicting values
    # be sure to use the tensorflow method for add and multiply,
    #so it happens in the learning env and added to the computation graph
    tf_failure_pred = tf.add(tf.multiply(tf_size_factor,tf_mq_data_size),tf_failure_offset)

    #3. Define the Loss Function (how much error) - mean squared error
    tf_fail_prob = tf.reduce_sum(tf.pow(tf_failure_pred - tf_failure, 2))/(2*num_train_samples)

    # Optimizer Learning Rate (Size of steps down the gradient)
    learning_rate = 0.1

    #

    #3. Define the Loss Function (how much error) - mean squared error
    tf_fail_prob = tf.reduce_sum(tf.pow(tf_failure_pred - tf_failure, 2))/(2*num_train_samples)

    # Optimizer Learning Rate (Size of steps down the gradient)
    learning_rate = 0.1

    #

    # 4. Define a Gradient optimizer that will minimize the loss defined in the operation "fail_prob"
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(tf_fail_prob)

    #Initialize the variables
    init = tf.global_variables_initializer()

    #Launch the Graph in the session (use with to define scope) (Note - if you do it this way, do everything in one block)
    with tf.Session() as sess:
        sess.run(init)
        # Set how often to display training progress and number of training iterations
        display_every = 3
        num_training_iter = 50 
        #keep iterating the training data
        for iteration in range(num_training_iter):
            #fit all training data
            for(x,y) in zip(train_mq_data_size_norm, train_failure_norm):
                sess.run(optimizer, feed_dict={tf_mq_data_size:x, tf_failure:y})
            #peridocially display the fail_prob, which is the error
            if (iteration + 1) % display_every == 0:
                c = sess.run(tf_fail_prob, feed_dict={tf_mq_data_size: train_mq_data_size_norm, tf_failure:train_failure_norm})
                print("iteration #:", '%04d' % (iteration + 1), "fail_prob=", "{:.9f}".format(c), \
                    "MQ_VAR=", sess.run(tf_size_factor), "failure_offset", sess.run(tf_failure_offset))
        print("Optimization finished!")
        training_fail_prob = sess.run(tf_fail_prob, feed_dict={tf_mq_data_size: train_mq_data_size_norm, tf_failure: train_failure_norm})
        print("trained fail_prob=", training_fail_prob,
        "MQ_VAR=", sess.run(tf_size_factor),
        "failure_offset=", sess.run(tf_failure_offset), '\n')

    #

        #Plot of training and test data, and learned regression

        #Get values used to normalized data so we can denormalize data back to its origional scale
        train_mq_data_size_mean = train_mq_data_size.mean()
        train_mq_data_size_std = train_mq_data_size.std()

        train_failure_mean = train_failure.mean()
        train_failure_std = train_failure.std()

        #plot the graph
        plt.rcParams["figure.figsize"] = (10,8)
        plt.figure()
        plt.ylabel("Failure")
        plt.xlabel("MQ_VAR")
        plt.plot(train_mq_data_size, train_failure, 'go', label='Training data')
        plt.plot(test_mq_data_size, test_mq_data_failure, 'mo', label='Testing data')
        plt.plot(train_mq_data_size_norm * train_mq_data_size_std + train_mq_data_size_mean,
        (sess.run(tf_size_factor) * train_mq_data_size_norm + sess.run(tf_failure_offset)) * train_failure_std + train_failure_mean,
        label='Learned Regression')

        plt.legend(loc='upper left')
        plt.show()

        app.run(debug=True, host='0.0.0.0')