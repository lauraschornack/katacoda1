Our goal is to send the output of running the ML model to an endpoint instead of standard out.

We will use the flask framework to create this endpoint, giving our model an "interface".

We need to be sure that what we are returning to the flask implementation of the flask framework is what was previously being returned to the command line.  

Click on the command below to open the code post-flask.  
Note, the flask code is commented out. 
`hello-post-flask.py`{{open}}