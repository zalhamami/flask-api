from app.model import ma, ma_field


class UserSchema(ma.Schema):
  id = ma_field.Integer(dump_only=True)
  username = ma_field.Str(required=True)


class UserCredentialSchema(ma.Schema):
  username = ma_field.Str(required=True)
  password = ma_field.Str(required=True, load_only=True)
