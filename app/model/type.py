from app.model import db

class TypeModel(db.Model):
  __tablename__ = 'types'

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  name = db.Column(db.String(255), nullable=False)

