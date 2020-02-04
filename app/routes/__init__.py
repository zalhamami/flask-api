from app.controller.type import Type, TypeList
from app.controller.user import UserList, UserLogin

def routes(app, api):
  # set version url
  VERSION_URL = '/' + app.config['API_VERSION'] + '/'

  @app.route('/ping')
  def ping():
    return 'All good.'

  # API Resources
  api.add_resource(Type, VERSION_URL + 'type/<int:id>')
  api.add_resource(TypeList, VERSION_URL + 'type')
  api.add_resource(UserList, VERSION_URL + 'user')
  api.add_resource(UserLogin, VERSION_URL + 'auth')