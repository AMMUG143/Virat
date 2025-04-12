
from login_page import login_page

def test_login_page(monkeypatch):
    # Mock the input function to simulate user input
    monkeypatch.setattr('builtins.input', lambda _: 'test_user')
    
    # Mock the authenticate function to always return True
    def mock_authenticate(username, password):
        return True
    
    monkeypatch.setattr('login_page.authenticate', mock_authenticate)
    
    # Call the login_page function
    login_page()