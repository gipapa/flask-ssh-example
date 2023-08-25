# flask-ssh

## **Description**
Sample web application to show how to stream the application's output from ssh connection.

## **To Use**
```
$ pip install -r requirements.txt
$ vim app/__init__.py  # Set your private ssh key and target host
$ FLASK_APP=./flask-ssh.py FLASK_DEBUG=1 flask run
```

##build command
gunicorn flask-ssh:app

##need to start sshd first, and then this repo can redirect ssh-strean to frontend
