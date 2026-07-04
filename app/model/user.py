from werkzeug.security import check_password_hash, generate_password_hash

from app.model import db


class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  username = db.Column(db.String(255), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)

  def set_password(self, password):
    """Store a salted hash of the given plaintext password."""
    self.password = generate_password_hash(password)

  def check_password(self, password):
    """Return True when the plaintext password matches the stored hash."""
    return check_password_hash(self.password, password)
