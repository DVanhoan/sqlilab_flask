import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
    DATABASE = os.environ.get("DATABASE", os.path.join(os.path.dirname(__file__), "..", "demo.db"))
    DEBUG = True
