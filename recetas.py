from reactivos import Reactivo

class Recetas:
    def __init__(self, id, nombre, objetivo, reactivos_utilizados, procedimiento, valores_a_medir):
        
        self.id = id
        self.nombre = nombre
        self.objetivo = objetivo
        self.reactivos_utilizados = reactivos_utilizados
        self.procedimiento = procedimiento
        self.valores_a_medir = valores_a_medir
        
  
    def show_attr(self):
        
        print("Informacion de recetas: ")
        print(f"ID: {self.id}")
        print(f"Nombre {self.nombre}")
        print(f"Objetivo: {self.objetivo}\n")
         
        print("Reactivos utilizados:")
        for i in self.reactivos_utilizados:
            for j, x in i.items():
                print(f"{j}: {x}")
                
        print("\n")      
        print("Procedimiento: ")
        for i in self.procedimiento:
            print(f"-> {i}")
        print("\n")
        
        print("Valores a medir: ")
        for i in self.valores_a_medir:
            for j, x in i.items():
                print(f"{j} - {x}")
       
       

        