import json

from app import db  
from app.repository.user import UserRepository
from app.helper.error_handler import ErrorHandler
from app.schema.user import UserSchema

class UserService:
  @classmethod
  def getAllData(cls, page_position, page_size, filter = None):
    # get data from repository
    data = UserRepository.getAll(
      page_position = page_position,
      page_size = page_size,
      filter = filter
    )
    return data

  @classmethod
  def getDataById(cls, id):
    # get data from repository
    data = UserRepository.getById(id)
    return data

  @classmethod
  def getDataByUsername(cls, username):
    # get data from repository
    data = UserRepository.getByUsername(username)
    return data

  @classmethod
  def insertData(cls, payload):
    data = UserRepository(
      name = payload['Username']
    )
    try:
      data.save()
    except:
      ErrorHandler.insertError('user')
    return data
    
  @classmethod
  def updateData(cls, data, payload):
    try:
      data.name = payload['User']
      db.session.commit()
    except:
      ErrorHandler.updateError('username')
    return 'ok'

  @classmethod
  def serialization(cls, data, many = False):
    result = UserSchema(many=many).dumps(data).data
    result = json.loads(result)
    return result