import os
from oauth2client import client


basedir = os.path.abspath(os.path.dirname(__file__))

class Auth:
    CLIENT_ID = 'CLIENT_ID'
    CLIENT_SECRET = 'CLIENT_SECRET'
    REDIRECT_URI = 'http://localhost:5000/oauth2callback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
    ACCESS = 'offline'
    HD= "olapic.com"


class Config:
    APP_NAME = "DNA"
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")


class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "default": DevConfig
}
credentials = client.OAuth2Credentials
flow = client.OAuth2WebServerFlow(Auth.CLIENT_ID, Auth.CLIENT_SECRET, Auth.SCOPE, redirect_uri=Auth.REDIRECT_URI)

auth_uri = flow.step1_get_authorize_url()
def greatExchange(code):
    return flow.step2_exchange(code)


