from app.repository.user import UserRepository


def test_register_creates_user_with_hashed_password(client, app):
  response = client.post('/v1/user', json={'username': 'bob', 'password': 'pw12345'})

  assert response.status_code == 201
  body = response.get_json()
  assert body['username'] == 'bob'
  assert 'password' not in body

  with app.app_context():
    stored = UserRepository.getByUsername('bob')
    assert stored.password != 'pw12345'
    assert stored.check_password('pw12345')


def test_register_rejects_duplicate_username(client, registered_user):
  response = client.post('/v1/user', json=registered_user)

  assert response.status_code == 409


def test_register_requires_username_and_password(client):
  response = client.post('/v1/user', json={'username': 'no-password'})

  assert response.status_code == 400
  assert 'password' in response.get_json()['errors']


def test_login_returns_tokens_for_valid_credentials(client, registered_user):
  response = client.post('/v1/auth', json=registered_user)

  assert response.status_code == 200
  body = response.get_json()
  assert body['access_token']
  assert body['refresh_token']


def test_login_rejects_wrong_password(client, registered_user):
  response = client.post(
    '/v1/auth',
    json={'username': registered_user['username'], 'password': 'wrong'}
  )

  assert response.status_code == 401
