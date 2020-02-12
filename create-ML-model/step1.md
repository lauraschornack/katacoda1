The first phase in ML Development is 
DATA
![ML Integration Flow](/laura-schornack/scenarios/create-ML-model/DATA.PNG)


Collecting and transforming data usually takes 70% of the time of your project.  

For the purposes of this scenario, we will generate our data with a python random number generator.  
The numbers that we generate will range from 1000 to 3500 and will contain 160 datapoints.  

    num_mq_data = 160
    np.random.seed(42)
    mq_data_size = np.random.randint(low=1000, high=3500, size=num_mq_data)
    np.random.seed(42)
    mq_data_failure = mq_data_size * 100.0 + np.random.randint(low=20000, high=70000, size=num_mq_data)

    plt.plot(mq_data_size, mq_data_failure, "bx")
    plt.ylabel("Failure")
    plt.xlabel("MQ_VAR")
    plt.show()

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
