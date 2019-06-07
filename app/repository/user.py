from app.model import db
from app.model.user import UserModel
from app.service.model import ModelService

class UserRepository(UserModel):
  @classmethod
  def getAll(cls, page_position, page_size, filter = None):
    result = ModelService.getAllData(cls, page_position, page_size, filter)
    return result

  @classmethod
  def getById(cls, id):
    result = cls.query.filter(cls.id == id).first()
    return result

  @classmethod
  def getByUsername(cls, username):
    result = cls.query.filter(cls.username == username).first()
    return result
    
  def save(self):
    db.session.add(self)
    db.session.flush()
    db.session.commit()
    