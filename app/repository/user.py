from app.model.user import UserModel
from app.repository.base import BaseRepository


class UserRepository(UserModel, BaseRepository):
  @classmethod
  def getByUsername(cls, username):
    return cls.query.filter(cls.username == username).first()
