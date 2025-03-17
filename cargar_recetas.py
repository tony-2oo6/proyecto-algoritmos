from recetas import Recetas

class Gestion_recetas():

    def crear_recetas(app,recetas_json):
        recetas_objetos=[]
        for receta in recetas_json:
            recetas_objetos.append(Recetas(receta["id"], receta["nombre"], receta["objetivo"], receta["reactivos_utilizados"], receta["procedimiento"], receta["valores_a_medir"]))
        app.recetas = recetas_objetos
        return recetas_objetos