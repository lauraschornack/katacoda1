The first phase in ML Development is 
DATA

![ML Integration Flow](/laura-schornack/scenarios/set-up/assets/data.png)

Collecting and transforming data usually takes 70% of the time of your project.  

For the purposes of this scenario, we will generate our data with a python random number generator.  
The numbers that we generate will range from 1000 to 3500 and will contain 160 datapoints.  

    num_mq_data = 160
    np.random.seed(42)
    mq_data_size = np.random.randint(low=1000, high=3500, size=num_mq_data)
    np.random.seed(42)
    mq_data_failure = mq_data_size * 100.0 + np.random.randint(low=20000, high=70000, size=num_mq_data)

 