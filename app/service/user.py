from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.repository.user import UserRepository
from app.helper.error_handler import ErrorHandler
from app.schema.user import UserSchema


class UserService:
  @classmethod
  def getAllData(cls, page_position, page_size, filter=None):
    return UserRepository.getAll(
      page_position=page_position,
      page_size=page_size,
      filter=filter
    )

  @classmethod
  def getDataById(cls, id):
    return UserRepository.getById(id)

  @classmethod
  def getDataByUsername(cls, username):
    return UserRepository.getByUsername(username)

  @classmethod
  def insertData(cls, payload):
    if cls.getDataByUsername(payload['username']):
      ErrorHandler.itemExists(payload['username'], 'user')

    user = UserRepository(username=payload['username'])
    user.set_password(payload['password'])
    try:
      user.save()
    except SQLAlchemyError:
      db.session.rollback()
      ErrorHandler.insertError('user')
    return user

  @classmethod
  def serialization(cls, data, many=False):
    return UserSchema(many=many).dump(data)
