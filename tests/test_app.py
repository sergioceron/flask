
import pytest
from flask import Flask, redirect as global_redirect


@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route("/old")
    def old():
        return app.redirect("/new")

    @app.route("/new")
    def new():
        return "Welcome to the new page!"

    return app


def test_redirect(app, client):
    
    with app.test_request_context():
        # Test redirect from /old to /new using the app's redirect method
        response = client.get("/old")
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/new")

        # Test arriving at the /new
        response = client.get("/new")
        assert response.status_code == 200
        assert response.data == b"Welcome to the new page!"
