from datetime import datetime

class Reactivo:
    def __init__(self,id, nombre, descripcion, costo, categoria, inventario_disponible, unidad_medida,fecha_caducidad,minimo_sugerido,conversiones_posibles):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.costo=costo
        self.categoria=categoria
        self.inventario_disponible=inventario_disponible
        self.unidad_medida=unidad_medida
        self.fecha_caducidad= datetime.strptime(fecha_caducidad, "%Y-%m-%d")
        self.minimo_sugerido=minimo_sugerido
        self.conversiones_posibles=conversiones_posibles
        
    def show_attr(self):
      
        print("Atributos del Reactivo:")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Costo: {self.costo}")
        print(f"Categoría: {self.categoria}")
        print(f"Inventario Disponible: {self.inventario_disponible}")
        print(f"Unidad de Medida: {self.unidad_medida}")
        print(f"Fecha de Caducidad: {self.fecha_caducidad}")
        print(f"Mínimo Sugerido: {self.minimo_sugerido}")
        print("Conversiones posibles:")
        for i in self.conversiones_posibles:
            for unidad, factor in i.items():
                print(f"{unidad}: {factor}")
        print("\n")


    def crear_reactivos(lista_reactivos):
        
        id = len(lista_reactivos)+1
        nombre = input("introduce el nombre del reactivo: ")
        descripcion = input("introduce la descripcion del reactivo: ")
        costo = float(input("introduce el costo del reactivo: "))
        categoria = input("introduce la categoria del reactivo: ")
        inventario_disponible = int(input("introduce la cantidad de inventario que tiene el reactivo: "))
        unidad_medida = input("introduce la unidad de medida: ")
        fecha_caducidad_str = input("Ingresa la fecha de caducidad (YYYY-MM-DD): ")
        if fecha_caducidad_str:
            fecha_caducidad = datetime.strptime(fecha_caducidad_str, "%Y-%m-%d")
        else:
            fecha_caducidad = datetime.max
    
        minimo_sugerido = float(input("introduce el minimo sugerido: "))
        conversiones = int(input("Introduce el número de conversiones posibles: "))
        conversiones_posibles = []
        for _ in range(conversiones):
            unidad = input("Introduce la unidad del reactivo: ")
            factor = float(input("Introduce el factor del reactivo: ")) 
            conversiones_posibles.append((unidad, factor))
      
        reactivo_nuevo = Reactivo(id, nombre, descripcion, costo, categoria, inventario_disponible, unidad_medida, fecha_caducidad, minimo_sugerido, conversiones_posibles)
        lista_reactivos.append(reactivo_nuevo)
        return reactivo_nuevo, lista_reactivos

        
    def editar_reactivo(self, nombre, atributo, nuevo_valor):

        nombre = input("Nombre del reactivo a editar: ")
        atributo = input("Atributo del reactivo a editar: ")
        nuevo_valor = input("Valor nuevo del atributo: ")
        for reactivo in self.reactivos:
            if reactivo.nombre == nombre:
                if hasattr(reactivo, atributo):
                    setattr(reactivo, atributo, nuevo_valor)
                    print(f'Atributo "{atributo}" del experimento "{nombre}" actualizado a "{nuevo_valor}"')
                else:
                    print(f'El atributo "{atributo}" no existe en el experimento "{nombre}"')
                return
        print(f'No se encontró un reactivo con el nombre "{nombre}"')

        for reactivo in self.reactivos:
            if reactivo.id == id:
                reactivo.editar_atributo(atributo, nuevo_valor)
                return
            print(f'No se encontró un reactivo con id: {id}')
                
    # def eliminar(self, lista_reactivos):
        

    #     id_eliminar = int(input("introduce el id del reactivo que deseas eliminar: "))
    #     for reactivo in lista_reactivos:
    #         if reactivo.id == id_eliminar:
    #             lista_reactivos.remove(reactivo)
    #             print(f"Experimento ({id_eliminar}) eliminado correctamente.\n")
    #             return 
    #         else:
    #             print("ID no encontrado.\n")
    #             return 
    
    def eliminar(self, lista_reactivos):
        
        id_eliminar = int(input("Introduce el ID del reactivo que deseas eliminar: "))
    
        for reactivo in lista_reactivos:
            if reactivo.id == id_eliminar:
                lista_reactivos.remove(reactivo)
                print(f"Reactivo con ID {id_eliminar} eliminado correctamente.\n")
                return  
    
            print("ID no encontrado.\n")

    
        
    def esta_vencido(self):
        if datetime.now() > self.fecha_caducidad:
            print(f"El reactivo {self.nombre} esta vencido")

    def dias_para_vencer(self):
        diferencia = self.fecha_caducidad - datetime.now()
        return diferencia.days
        
        
    def verificar_inventario_min(self, minimo):
        for reactivo in self.reactivos:
            if reactivo.inventario < minimo:
                print(f"¡Advertencia! El reactivo {reactivo.nombre} está por debajo del mínimo.")
                
    def cambiar_medida(self,lista_reactivos):
        pass
    #     k = int(input("Ingrese el número del reactivo a editar: "))

    #     if 1 <= k <= len(lista_reactivos):  
    #         reactivo_a_convertir = lista_reactivos[k - 1]  

    #         print(f"\n **Unidades de Conversión Disponibles para {reactivo_a_convertir['nombre']}:**")
            
            
    #         for conversion in reactivo_a_convertir["conversiones_posibles"]:
    #             print(f"- {reactivo_a_convertir['unidad_medida']} → {conversion['unidad']} (Factor: {conversion['factor']})")
            
    #     else:
    #         print("⚠️ Número de reactivo inválido. Inténtelo de nuevo.")


        #     medida = float(input("introduce la cantidad actual de reactivo"))
        #     conversion = input("A cual unidad quiere convertir la medida: \n1-ml \n2-l \n3-g \n4-kg ")
            
        #     if conversion == "1":
                
        #         conversion_L_a_ml = medida * 1000/1
                
        #         print(f"la conversion final es: {conversion_L_a_ml}")
                
                
        #     elif conversion =="2":
                
        #         conversion_ml_a_L = medida * 1/1000
        #         print(f"la nueva conversion es: {conversion_ml_a_L}")
                
        #     elif conversion =="3":
                
        #         conversion_g_a_kg = medida * 1/1000
                
        #         print(f"la nueva conversion es: {conversion_g_a_kg}")
            
        #     elif conversion =="4":
            
        #         conversion_kg_a_g = medida * 1000/1
                
        #         print(f"la nueva conversion es: {conversion_kg_a_g}")
                
        # else:
        #     print("Error el numero no puede ser negativo")
        #     pass
            
            
      