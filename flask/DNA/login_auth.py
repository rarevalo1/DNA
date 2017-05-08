import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Auth:
    CLIENT_ID = '168948954860-sm4gvd8tpgrqu7hrcfshk75vpkupktvd.apps.googleusercontent.com'
    CLIENT_SECRET = '6a8nDtj8tjr4Ioop9jIwSs0t'
    REDIRECT_URI = 'https://localhost:5000/oauth2callback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = 'https://www.googleapis.com/auth/userinfo.email'


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