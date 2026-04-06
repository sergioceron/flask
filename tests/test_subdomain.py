import pytest
from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)
    app.config['SERVER_NAME'] = 'example.com'

    subdomain_bp = Blueprint('subdomain', __name__, subdomain='foo', url_prefix='/')

    @subdomain_bp.route('/')
    def index():
        return 'Hello from foo'

    app.register_blueprint(subdomain_bp)

    return app


def test_subdomain_route():
    app = create_app()
    client = app.test_client()

    response = client.get('/', base_url='http://foo.example.com')
    assert response.status_code == 200
    assert response.data == b'Hello from foo'
