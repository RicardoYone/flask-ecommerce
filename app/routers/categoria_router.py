from app import app
from flask import request
from app.controllers.categoria_controller import CategoriaController


@app.route("/categorias/", methods=['GET', 'POST'])
def categorias():
    if request.method == 'GET':
        categorias = CategoriaController().getAll()
        return categorias
    else:
        pass
