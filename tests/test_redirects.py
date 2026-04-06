import pytest
from flask import Flask, redirect, url_for


def test_default_redirect(client):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return redirect(url_for('target'))

    @app.route('/target')
    def target():
        return 'target'

    with app.test_client() as client:
        rv = client.get('/', follow_redirects=False)
        assert rv.status_code == 302
        assert rv.headers['Location'] == 'http://localhost/target'


def test_redirect_with_302_status(client):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return redirect(url_for('target'), 302)

    @app.route('/target')
    def target():
        return 'target'

    with app.test_client() as client:
        rv = client.get('/', follow_redirects=False)
        assert rv.status_code == 302
        assert rv.headers['Location'] == 'http://localhost/target'


def test_redirect_with_301_status(client):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return redirect(url_for('target'), 301)

    @app.route('/target')
    def target():
        return 'target'

    with app.test_client() as client:
        rv = client.get('/', follow_redirects=False)
        assert rv.status_code == 301
        assert rv.headers['Location'] == 'http://localhost/target'


def test_redirect_with_custom_scheme(client):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return redirect('ftp://example.com/resource', 301)

    with app.test_client() as client:
        rv = client.get('/', follow_redirects=False)
        assert rv.status_code == 301
        assert rv.headers['Location'] == 'ftp://example.com/resource'
