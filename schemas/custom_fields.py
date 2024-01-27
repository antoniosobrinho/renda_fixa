from marshmallow import fields, ValidationError

class IntegerField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if not isinstance(value, int):
            raise ValidationError('Campo deve ser um número inteiro')
        return value
        
class FloatField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if not isinstance(value, float):
            raise ValidationError('Campo deve ser um número decimal')
        return value