from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Irina", lastname="Ivanova", homenumber="84997774747", mobilenumber="89051114512"))
    app.logout()

