from app.model import db
from app.model.type import TypeModel
from app.service.model import ModelService

class TypeRepository(TypeModel):
  @classmethod
  def getAll(cls, page_position, page_size, filter = None):
    result = ModelService.getAllData(cls, page_position, page_size, filter)
    return result

  @classmethod
  def getById(cls, id):
    result = cls.query.filter(cls.id == id).first()
    return result

  def save(self):
    db.session.add(self)
    db.session.flush()
    db.session.commit()
    