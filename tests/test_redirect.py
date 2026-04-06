
import pytest
from flask import Flask, redirect, url_for


def test_redirect_default_code(app):
    @app.route('/old')
    def old_route():
        return redirect(url_for('new_route'))

    @app.route('/new')
    def new_route():
        return "New Route"

    client = app.test_client()
    response = client.get('/old')
    assert response.status_code == 302
    assert response.location == 'http://localhost/new'


def test_redirect_custom_code(app):
    @app.route('/temp')
    def temporary():
        return redirect(url_for('permanent'), code=307)

    @app.route('/permanent')
    def permanent():
        return "Permanent Route"

    client = app.test_client()
    response = client.get('/temp')
    assert response.status_code == 307
    assert response.location == 'http://localhost/permanent'


def test_redirect_with_anchor(app):
    @app.route('/anchor_test')
    def anchor_test():
        return redirect(url_for('target', _anchor='section2'))

    @app.route('/target')
    def target():
        return "Target Route"

    client = app.test_client()
    response = client.get('/anchor_test')
    assert response.status_code == 302
    assert response.location == 'http://localhost/target#section2'


@pytest.fixture
 def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app
