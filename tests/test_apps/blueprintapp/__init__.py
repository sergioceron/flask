from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True
from blueprintapp.apps.admin import admin_bp
from blueprintapp.apps.frontend import frontend_bp

app.register_blueprint(admin_bp)
app.register_blueprint(frontend_bp)
