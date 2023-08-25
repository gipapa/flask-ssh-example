from flask import Flask

__all__ = 'app'.split()

app = Flask(__name__)
from . import routes  # NOQA

app.config['SSH_USERNAME'] = "root"
app.config['SSH_HOSTNAME'] = "web-p174.onrender.com"
app.config['SSH_PRIV_KEY'] = """
-----BEGIN RSA PRIVATE KEY-----
root5566
-----END RSA PRIVATE KEY-----
"""
