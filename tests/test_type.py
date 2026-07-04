def test_create_type_returns_created_status(client):
  response = client.post('/v1/type', json={'name': 'widget'})

  assert response.status_code == 201
  body = response.get_json()
  assert body['name'] == 'widget'
  assert body['id']


def test_create_type_validates_payload(client):
  response = client.post('/v1/type', json={})

  assert response.status_code == 400
  assert 'name' in response.get_json()['errors']


def test_get_type_by_id(client):
  created = client.post('/v1/type', json={'name': 'gadget'}).get_json()

  response = client.get('/v1/type/{0}'.format(created['id']))

  assert response.status_code == 200
  assert response.get_json()['name'] == 'gadget'


def test_get_missing_type_returns_not_found(client):
  response = client.get('/v1/type/999')

  assert response.status_code == 404


def test_update_type(client):
  created = client.post('/v1/type', json={'name': 'old'}).get_json()

  response = client.put('/v1/type/{0}'.format(created['id']), json={'name': 'new'})

  assert response.status_code == 200
  assert response.get_json()['name'] == 'new'


def test_list_types_includes_pagination_meta(client):
  for name in ('a', 'b', 'c'):
    client.post('/v1/type', json={'name': name})

  response = client.get('/v1/type?page_size=2&page_position=1')

  assert response.status_code == 200
  meta = response.get_json()['Meta']
  assert meta['TotalData'] == 3
  assert meta['TotalPage'] == 2
  assert meta['PageSize'] == 2
