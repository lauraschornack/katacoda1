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
