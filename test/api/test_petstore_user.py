# Library
import pytest           # Unit test framework
import requests         # API test framework - Request / Response

# API address
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
# Test
def test_create_user():
    # Settings
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1015'

    # Execute
    response = requests.post(                       # Post Request
        url=base_url,                               # API endpoint
        data=open('C:/Users/Vitor/Desktop/Vitor/Cursos/Python2023/PyIterasys/test/db/user1.json', 'rb'),      # Json Body
        headers=headers,                            # Header Content-Type
    )

    # Format
    response_body = response.json()
    print(response)                                 # Json response
    print(response.status_code)                     # Status Code
    print(response_body)                            # Format Response

    # Evaluate
    assert response.status_code == status_code_esperado
    assert response_body['code'] == codigo_esperado
    assert response_body['type'] == tipo_esperado
    assert response_body['message'] == mensagem_esperada
    
def test_check_user():
    # Settings
    status_code = 200
    id = 1015
    username = 'name'
    firstName = 'User'
    lastName = 'Name'
    email = 'user@mail.com'
    password = '123456'
    phone = 'string'
    userStatus = 0

    # Execute
    response = requests.get(
        url=base_url + '/' + username,
        headers=headers
    )
    # Format
    response_body = response.json()
    print(response)                         # Json response
    print(response.status_code)             # Status Code
    print(response_body)                    # Format Response

    # Evaluate
    assert response.status_code == status_code
    assert response_body['id'] == id
    assert response_body['username'] == username
    assert response_body['email'] == email
    assert response_body['phone'] == phone

def test_modify_user():
    # Settings
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    username = 'user'

    # Execute
    response = requests.put(                       # Get Request
        url=base_url + '/' + username,             # API endpoint
        data=open('C:/Users/Vitor/Desktop/Vitor/Cursos/Python2023/PyIterasys/test/db/user2.json', 'rb'),      # Json Body
        headers=headers,                            # Header Content-Type
    )

    # Format
    response_body = response.json()
    print(response)                                 # Json response
    print(response.status_code)                     # Status Code
    print(response_body)                            # Format Response

    # Evaluate
    assert response.status_code == status_code_esperado
    assert response_body['code'] == codigo_esperado
    assert response_body['type'] == tipo_esperado

def test_delete_user():
    # Settings
    username = 'name'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'name'

    # Execute
    response = requests.delete(
        url=base_url + '/' + username,
        headers=headers
    )
    # Format
    response_body = response.json()
    print(response)                         # Json response
    print(response.status_code)             # Status Code
    print(response_body)                    # Format Response

    # Evaluate
    assert response.status_code == status_code_esperado
    assert response_body['code'] == codigo_esperado
    assert response_body['type'] == tipo_esperado
    assert response_body['message'] == mensagem_esperada