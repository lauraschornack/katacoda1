
Now that we can run a simple docker container, the next scenario will walk us through how to create a simple model. 


------------(remove below)

`sess = tf.Session()`{{execute}}

`hello = tf.constant("Hello from tensorflow")`{{execute}}

`print(sess.run(hello))`{{execute}}

`a = tf.constant(20)`{{execute}}

`b = tf.constant(22)`{{execute}}

`print('a + B = {0}'.format(sess.run(a+b)))`{{execute}}