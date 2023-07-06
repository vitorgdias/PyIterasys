# Library
import time

import pytest           # Unit test framework
import requests         # API test framework - Request / Response
# API address
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
user_token = ''
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
    username = 'user'
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
    username = 'user'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1015'
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
    assert response_body['message'] == mensagem_esperada
def test_delete_user():
    # Settings
    username = 'user'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = username
    # Execute
    response = requests.delete(
        url=base_url + '/' + username,
        headers=headers
    )
    match response.status_code:
        case 200:                               # Delete the user
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
        case 400:
            print('Incorrect user')
        case 404:
            print('User not found')
def test_user_login():
    # Settings
    username = 'user'
    password = '123456'
    status_code_expected = 200
    code_expected = 200
    type_expected = 'unknown'
    first_message_expected = 'logged in user session:'
    # Execution
    response = requests.get(
        url=f'{base_url}/login?username={username}&password={password}',
        headers=headers
    )
    # Format
    response_body = response.json()
    print(response)
    print(response.status_code)
    print(response_body)
    # Evaluate
    assert response.status_code == status_code_expected
    assert response_body['code'] == code_expected
    assert response_body['type'] == type_expected
    assert response_body['message'].find(first_message_expected) != -1
    # Assert to verify if the message in response body contain the initial phrase
    # If the phrase don't have the words or sentences, -1 means false

    # Extract the token from response message
    response_message = response_body['message']
    user_token = response_message[23:37]
    print(f'User token is: {user_token}')
