import pytest
import requests
base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}
def test_create_pet():
    name_expected = 'Loki'
    status_code_expected = 200
    tag_expected = 'fluffy'
    response = requests.post(
        url=base_url,
        data=open('C:/Users/Vitor/Desktop/Vitor/Cursos/Python2023/PyIterasys/test/db/pet1.json', 'rb'),
        headers=headers
    )
    print(response)
    print(response.status_code)
    response_body = response.json()
    print(response_body)
    assert response.status_code == status_code_expected
    assert response_body['name'] == name_expected
    assert response_body['tags.name'] == tag_expected
