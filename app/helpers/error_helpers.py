from marshmallow import ValidationError


def campo_necesario(data):
    if not data:
        raise ValidationError("Data no proporcionado")
