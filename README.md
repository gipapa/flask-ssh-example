# flask-ssh

## **To Use**
```
$ pip install -r requirements.txt
$ vim app/__init__.py  # Set your private ssh key and target host
$ FLASK_APP=./flask-ssh.py FLASK_DEBUG=1 flask run
```
## gipapa note

### build command
```
gunicorn flask-ssh:app
```

1. Sample web application to show how to stream the application's output from ssh connection.
2. need to start sshd first, and then this repo can redirect ssh-strean to frontend
3. can deploy to some cloud-based resource like heroku, render 
