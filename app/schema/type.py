from app.model import ma, ma_field

class TypeSchema(ma.ModelSchema):
  Id = ma_field.Integer(attribute='id', dump_only=True)
  Name = ma_field.Str(attribute='name')

  class Meta:
    ordered = True