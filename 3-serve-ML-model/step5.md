We are now ready to complete the last step of the ML Code Cycle: Interface.

![ML Integration Cycle](interface2.jpg)

To give our model an interface for an application to connect to, we will give it a Flask Endpoint.

Add in Flask Code which will allow us to send the output to an endpoint instead of the command line.  

We need to be sure that what we are returning to the flask implementation of the flask framework is what was previously being returned to the command line.  

Uncomment the flask code so that we can run it.