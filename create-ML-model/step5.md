The next phase of Machine Learning Development is:
MODEL

![ML Integration Flow](/laura-schornack/scenarios/create-ML-model/assets/model.png)

    
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

