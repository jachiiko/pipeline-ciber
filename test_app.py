import sys
import os

# Asegurar que Jenkins vea el directorio actual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hola desde Flask - Pipeline funcionando!"
