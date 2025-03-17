import requests
from cargar_reactivos import Gestion_reactivos
from cargar_recetas import Gestion_recetas
from cargar_experimentos import Gestion_experimentos
from reactivos import Reactivo
from experimentos import Experimento
from datetime import datetime
import random



class App():

    def obtener_json(self,url, params = None):
        try:
            response = requests.get(url, params = params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al acceder a la API: {e}")
            return None


    def start(self):
        self.reactivos_json=self.obtener_json("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/reactivos.json")
        self.recetas_json=self.obtener_json("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/recetas.json")
        self.experimentos_json=self.obtener_json("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/experimentos.json")
    
        lista_recetas = Gestion_recetas.crear_recetas(self, self.recetas_json)
        lista_reactivos =  Gestion_reactivos.crear_reactivos(self,self.reactivos_json)
        lista_experimentos = Gestion_experimentos.crear_experimento(self, self.experimentos_json)
        
    
        while True:
            
            cuenta_de_experimentos = []
            
            print("""

              
============= MENU PRINCIPAL ==============
              

              """)
            
            pregunta1 = (input("¿Que opcion desea realizar? \n1-Mostrar Reactivos \n2-Mostrar Experimentos \n3-Mostrar Recetas \n4-Ver estadisticas \n5-Salir \n->"))
            
            if pregunta1 == "1":
                
                for i in self.reactivos:
                    i.show_attr()
                    
                    
                pregunta_reactivo = input("¿Que quieres hacer en reactivos? \n1-Crear Reactivo \n2-Editar Reactivo \n3-Eliminar reactivo \n4-Ver fecha de caducidad \n5-Atras \n->")
                    
                if pregunta_reactivo == "1":
                        
                    lista_reactivos = Reactivo.crear_reactivos(lista_reactivos)
                    print("¡El reactivo se agrego exitosamente!")
                    
                elif pregunta_reactivo == "2":
                        
                    Reactivo.editar_reactivo(self, None, None, None)
                    
                elif pregunta_reactivo == "3":
                        
                    Reactivo.eliminar(self, lista_reactivos)
                
                elif pregunta_reactivo == "4":
                    
                    print("Fechas de caducidad: \n")
                    for reactivo in self.reactivos:
                        if reactivo.esta_vencido():
                            print(f"- {reactivo.nombre} vencio el {reactivo.fecha_caducidad.date()}")
                        else:
                            print(f"- {reactivo.nombre} vence en {reactivo.dias_para_vencer()} días")
                            
                            
                elif pregunta1 == "5":
                    
                    pass
                        
            elif pregunta1 == "2":
                
                for i in self.experimento:
                    i.show_attr()
                    
                pregunta_experimento = input("¿Que quieres hacer en Experimentos? \n1-Realizar Experimento \n2-Crear Experimento \n3-Editar Experimento \n4-Eliminar Experimento \n5-Atras \n->")
                    
                if pregunta_experimento == "1":
                    
                    
                    Experimento.realizar_experimento(self.experimento, self.recetas, self.reactivos)
                    
                    
                elif pregunta_experimento == "2":
                
                    lista_experimentos = Experimento.crear_experimento(lista_experimentos, lista_recetas)
                    
                    
                elif pregunta_experimento == "3":
                    
                    Experimento.editar_experimento(self, None, None, None)

                    
                elif pregunta_experimento == "4":
                    

                    Experimento.eliminar_experimento(self, lista_experimentos)
                 
            
            elif pregunta1 == "3":
                
                for i in self.recetas:
                    i.show_attr()
                   
            
            elif pregunta1 == "4":
                
                pass
            
            
            elif pregunta1 == "5":
                
                print("¡Nos vemos pronto!")
                break