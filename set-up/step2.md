Option 1: Setup with containers:

For each step, either click on the highlighted text to run it in the terminal, or if you prefer, you can type it.  

Container Setup:

Step 1:
Pull down docker file from my git hub
`git clone https://github.com/lauraschornack/katacoda1.git`{{execute}}

Step 2:
`cd katacoda1/set-up`{{execute}}

The Docker file looks like this:
We are adding the following components into our container.
`katacoda1docker`{{open}}.

Step 3:
Build the docker file. 
`docker build . -t katacoda1docker`{{execute}}

Step 4:
`docker run -p 8500:8500 -it --rm katacoda1docker`{{execute}}


Render port 8500: https://[[HOST_SUBDOMAIN]]-8500-[[KATACODA_HOST]].environments.katacoda.com/

Render port 80: https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com/

Display page allowing user to select port:
https://[[HOST_SUBDOMAIN]]-[[KATACODA_HOST]].environments.katacoda.com/