from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Irina", lastname="Ivanova", homenumber="84997774747", mobilenumber="89051114512"))
    app.session.logout()

