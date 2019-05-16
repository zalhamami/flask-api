from app.model.type import TypeModel

class TypeRepository(TypeModel):
  @classmethod
  def getAll(cls):
    result = cls.query.all()
    return result

  @classmethod
  def getById(cls, id):
    result = cls.query.filter(cls.id == id).first()
    return result
