from app.model import ma, ma_field

class UserSchema(ma.ModelSchema):
  Id = ma_field.Integer(attribute='id', dump_only=True)
  Username = ma_field.Str(attribute='username')

  class Meta:
    ordered = True