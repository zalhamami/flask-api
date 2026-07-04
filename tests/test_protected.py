def test_user_list_requires_authentication(client):
  response = client.get('/v1/user')

  assert response.status_code == 401


def test_user_list_returns_data_with_valid_token(client, auth_headers):
  response = client.get('/v1/user', headers=auth_headers)

  assert response.status_code == 200
  body = response.get_json()
  assert 'Data' in body
  assert 'Meta' in body
