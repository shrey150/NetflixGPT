import os
from datetime import timedelta
from jose import jwt
import pytest
from app.auth import create_access_token, SECRET_KEY, ALGORITHM

# HOW TO RUN: poetry run pytest tests/test_auth.py

def test_create_access_token():
    data = {"sub": "testuser@example.com"}
    
    # Generate the JWT
    token = create_access_token(data)
    
    # Decode the JWT to verify its contents
    decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
    # Check that the expected data is in the token
    assert decoded_data["sub"] == data["sub"]
    
    # Check that the token contains an expiration time
    assert "exp" in decoded_data

def test_create_access_token_with_expiration():
    # Data to encode in the JWT
    data = {"sub": "testuser@example.com"}
    
    # Set a specific expiration time
    expires_delta = timedelta(minutes=5)
    
    # Generate the JWT
    token = create_access_token(data, expires_delta)
    
    # Decode the JWT to verify its contents
    decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
    # Check that the expected data is in the token
    assert decoded_data["sub"] == data["sub"]
    
    # Check that the token contains an expiration time
    assert "exp" in decoded_data
    
    # Check that the expiration time is within the expected range
    assert decoded_data["exp"] - decoded_data["iat"] <= expires_delta.total_seconds()


if __name__ == "__main__":
    pytest.main()
