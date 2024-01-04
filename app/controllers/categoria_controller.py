from app.models.categoria_model import CategoriaModel
from app.schemas.categoria_schema import category_schema, categories_schema
from app import app


class CategoriaController():
    def getAll():
        categories = CategoriaModel.query.all()
        result = categories_schema.dump(categories)
        return result, 200

    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
