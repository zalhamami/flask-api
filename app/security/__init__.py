from werkzeug.security import safe_str_cmp

from app.repository.user import UserRepository

def authenticate(username, password):
  user = UserRepository.getByUsername(username)
  if user and safe_str_cmp(user.password, password):
    return user

def identity(payload):
  id = payload['identity']
  user = UserRepository.getById(id)
  return user
