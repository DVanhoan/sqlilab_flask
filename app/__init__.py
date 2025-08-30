from flask import Flask
from .config import Config
from .db import init_app as init_db
from .blueprints.auth import bp as auth_bp
from .blueprints.products import bp as products_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_db(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)

    @app.route("/")
    def index():
        return (
            "<h3>SQL Injection Mini-Lab</h3>"
            "<ul>"
            "<li><a href='/vuln/login'>Vulnerable Login</a> | <a href='/safe/login'>Safe Login</a></li>"
            "<li><a href='/vuln/search'>Vulnerable Search</a> | <a href='/safe/search'>Safe Search</a></li>"
            "<li><a href='/vuln/products'>Vulnerable Products (ORDER BY)</a> | <a href='/safe/products'>Safe Products</a></li>"
            "</ul>"
            "<p>Use these paired pages to demonstrate SQL injection and its mitigations.</p>"
        )
    return app
