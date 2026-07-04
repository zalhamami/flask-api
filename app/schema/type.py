from app.model import ma, ma_field


class TypeSchema(ma.Schema):
  id = ma_field.Integer(dump_only=True)
  name = ma_field.Str(required=True)
