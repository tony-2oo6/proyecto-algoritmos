from experimentos import Experimento

class Gestion_experimentos():
    
    def crear_experimento(app, experimentos_json):
        experimento_objetos=[]
        for experimento in experimentos_json:
            experimento_objetos.append(Experimento(experimento["id"],experimento["receta_id"],experimento["personas_responsables"],experimento["fecha"],experimento["costo_asociado"],experimento["resultado"], veces_hecho=0))
        app.experimento=experimento_objetos
        return experimento_objetos