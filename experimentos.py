from reactivos import Reactivo
from recetas import Recetas
from datetime import datetime
import random 


class Experimento:
    def __init__(self, id, receta_id, personas_responsables, fecha, costo_asociado, resultado, veces_hecho):
        
        self.id = id
        self.receta_id = receta_id
        self.personas_responsables = personas_responsables
        self.fecha = fecha
        self.costo_asociado = costo_asociado
        self.resultado = resultado
        self.veces_hecho = 0
        
    def show_attr(self):
      
        print("experimetos:")
        print(f"ID: {self.id}")
        print(f"Receta id: {self.receta_id}")
        print(f"Personas responsables:")
        for persona in self.personas_responsables:
            print(f"{persona}")
        print(f"Fecha: {self.fecha}")
        print(f"Costo: {self.costo_asociado}")
        print(f"Resultado: {self.resultado}")
        print("\n")
        return 
    def crear_experimento(lista_experimentos, lista_recetas):
        
        
        id = len(lista_experimentos)+1
        receta_id = len(lista_recetas)+1
        personas_responsables = int(input("Introduce el número de personas responsables: "))
        personas_r = []
        for i in range(personas_responsables):
            personas = input("Introduce el nombre de las personas responsables: ")
            personas_r.append(personas)
            
        fecha = datetime.today().date()
        costo_asociado = float(input("Ingrese el costo: "))
        resultado = input("Ingrese el resultado del experimento: ")
        
        
        for reactivo in lista_experimentos:  
            if fecha > Reactivo(reactivo.fecha_caducidad):
                print(f"No se puede hacer el experimento por que el reactivo '{reactivo.nombre}' está vencido.")
            return None, lista_experimentos
        
        
        

        nuevo_experimento = Experimento(id, receta_id, personas_r, fecha, costo_asociado, resultado)
        lista_experimentos.append(nuevo_experimento)
        print("¡El experimento se creo con exito!")
        return nuevo_experimento, lista_experimentos
    
    
    def editar_experimento(self, nombre, atributo, nuevo_valor):

        nombre = input("Nombre del experimento a editar: ")
        atributo = input("Atributo del experimento a editar: ")
        nuevo_valor = input("Valor nuevo del atributo: ")
        for experimento in self.experimento:
            if experimento.nombre == nombre:
                if hasattr(experimento, atributo):
                    setattr(experimento, atributo, nuevo_valor)
                    print(f'Atributo "{atributo}" del experimento "{nombre}" actualizado a "{nuevo_valor}"')
                else:
                    print(f'El atributo "{atributo}" no existe en el experimento "{nombre}"')
                return
        print(f'No se encontró un experimento con el nombre "{nombre}"')

        for experimento in self.experimento:
            if experimento.id == id:
                experimento.editar_atributo(atributo, nuevo_valor)
                return
            else:
                print(f'No se encontró un experimento con id: {id}')
                return
    
    
    def eliminar_experimento(self, lista_experimento):
        
        id_a_eliminar = int(input("introduce el id del experimento que deseas eliminar: "))
        for experimento in lista_experimento:
            if experimento.id == id_a_eliminar:
                lista_experimento.remove(experimento)
                print(f"Experimento ({id_a_eliminar}) eliminado correctamente.\n")
                return 
            
            print("ID no encontrado.\n")
            return 
    
   
    def validar_fecha_caducidad(fecha_caducidad):
      
        fecha_caducidad = datetime.strptime(fecha_caducidad, '%Y-%m-%d')
        fecha_actual = datetime.now()
        if fecha_caducidad >= fecha_actual:
            return True
        elif fecha_caducidad < fecha_actual:
            
            return False
        else:
            print('Formato de fecha incorrecto. Use el formato YYYY-MM-DD.')   
            return False    
    
    def realizar_experimento(experimentos, recetas, reactivos):

        id_experimento_hacer = input('Ingrese el ID del experimento a realizar: ')

        try:
            id_experimento_hacer = int(id_experimento_hacer)
        except ValueError:
            print('El ID debe ser un número entero.')
            return

        experimento_encontrado = None
        for exp in experimentos:
            if exp.id == id_experimento_hacer:
                experimento_encontrado = exp
                break
           
        if not experimento_encontrado:
            print(f'No se encontró un experimento con el ID {id_experimento_hacer}')
            return


        experimento_encontrado.veces_hecho += 1

        receta_encontrada = None
        for r in recetas:
            if r.id == experimento_encontrado.id:
                receta_encontrada = r
                break

        if not receta_encontrada:
            print(f'No se encontró una receta con ID {experimento_encontrado.id}')
            return

        costo_total = 0.0

        for reactivo_usado in receta_encontrada.reactivos_utilizados:
            reactivo_id = reactivo_usado['reactivo_id']
            cantidad_necesaria = reactivo_usado['cantidad_necesaria']
            unidad_medida = reactivo_usado['unidad_medida']

            reactivo_encontrado = None
            for r in reactivos:
                if r.id == reactivo_id:
                    reactivo_encontrado = r
                    break

            if not reactivo_encontrado:
                print(f'No se encontró un reactivo con ID {reactivo_id}')
                continue

            fecha_caducidad = reactivo_encontrado.fecha_caducidad
        
            if not Experimento.validar_fecha_caducidad(fecha_caducidad):
                print('La fecha de caducidad del experimento ya se vencio no se puede realizar')
                return

            error = random.uniform(0.001, 0.225)
            cantidad_errada = cantidad_necesaria * error

            if reactivo_encontrado.unidad_medida == unidad_medida:
                cantidad_total_consumida = cantidad_necesaria + cantidad_errada
            else:
                conversion_obj = None
                for c in reactivo_encontrado.conversiones_posibles:
                    if c['unidad'] == unidad_medida:
                        conversion_obj = c
                        break

                if not conversion_obj:
                    print(f'No se encontró una conversión para la unidad {unidad_medida}.')
                    continue

                cantidad_convertida = cantidad_necesaria / conversion_obj['factor']
                cantidad_errada_convertida = (cantidad_necesaria * error) / conversion_obj['factor']
                cantidad_total_consumida = cantidad_convertida + cantidad_errada_convertida

            reactivo_encontrado.inventario_disponible -= cantidad_total_consumida

            costo_unitario = reactivo_encontrado.costo
            costo_parcial = cantidad_total_consumida * costo_unitario
            costo_total += costo_parcial

        experimento_encontrado.costo_asociado += costo_total

        print("Experimento realizado exitosamente.")
        print(f"El costo adicional sumado a este experimento es: {costo_total:.2f}")
        print(f"Costo total acumulado para este experimento: {experimento_encontrado.costo_asociado:.2f}")

    #     # 8) Guardar la lista de experimentos en un .txt (contenido JSON)
    #     guardar_experimentos_json(experimentos)


    # def guardar_experimentos_json(experimentos, nombre_archivo="experimentos.txt"):
    #     """
    #     Convierte la lista de objetos Experimento a dict y la guarda en un archivo TXT usando JSON.
    #     """
    #     # Convertir cada Experimento en dict
    #     lista_experimentos_dict = [exp.to_dict() for exp in experimentos]

    #     # Guardarlo en un archivo
    #     with open(nombre_archivo, "w", encoding="utf-8") as f:
    #         json.dump(lista_experimentos_dict, f, indent=4, ensure_ascii=False)

    #     print(f"Los experimentos se han guardado en {nombre_archivo} con formato JSON.")