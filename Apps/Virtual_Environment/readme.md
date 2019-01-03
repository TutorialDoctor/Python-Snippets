Resource: https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

You'll need to install virtualenv: https://virtualenv.pypa.io/en/latest/installation/

To create a virtual environemt folder from your proejct folder (already done in this case):

~~`virtualenv env`~~

To make pip easier to run (do this every time you restart the terminal):

`source env/bin/activate`

If you want to check the python path of the virtual environment:

`which python3`

**To run the app from the Virtual_Environment directory:**

`python3 app.py`

Since you've activated the source you can now do:

`pip3 install ...`

To install modules from the requirements file into the virtual environment do:

`env/bin/pip install -r requirements.txt`

This is helpful also:

https://www.enigmeta.com/blog/starting-flask/

