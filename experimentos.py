from reactivos import Reactivo
from recetas import Recetas
from datetime import datetime
import random 


class Experimento:
    def __init__(self, id, receta_id, personas_responsables, fecha, costo_asociado, resultado):
        
        self.id = id
        self.receta_id = receta_id
        self.personas_responsables = personas_responsables
        self.fecha = fecha
        self.costo_asociado = costo_asociado
        self.resultado = resultado
        
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
    
   

    def realizar_experimento(self):
        id_experimento_hacer = input('Ingrese el ID del experimento a realizar: ')

        try:
            id_experimento_hacer = int(id_experimento_hacer)
        except ValueError:
            print('El ID debe ser un número entero')
            return

        experimento_encontrado = None
        for experimento in self.experimento:
            if experimento.id == id_experimento_hacer:
                experimento_encontrado = experimento
                

        if not experimento_encontrado:
            print(f'No se encontró un experimento con el ID {id_experimento_hacer}')
            return

        # Validar fecha de caducidad del experimento
        try:
            fecha_caducidad_dt = datetime.strptime(experimento_encontrado.fecha, '%Y-%m-%d')
            fecha_actual = datetime.now()
            print(experimento_encontrado.show_attr())
            if fecha_caducidad_dt < fecha_actual:
                print('La fecha de caducidad del experimento ya ha pasado, no se puede realizar el experimento')
                return
        except ValueError:
                print('Formato de fecha incorrecto. Use el formato YYYY-MM-DD')
                return

        # Aumentar el contador de veces que se ha realizado
        experimento_encontrado['veces_hecho'] += 1

        # Buscar la receta asociada
        receta_encontrada = None
        for receta in self.recetas_json:
            if receta.id == experimento_encontrado.id:
                receta_encontrada = receta
                

        if not receta_encontrada:
            print(f'No se encontró una receta con ID {experimento_encontrado["receta_id"]}')
            return

        # Inicializamos el costo total del experimento en 0
        costo_total_experimento = 0.0

        # Recorrer los reactivos que se usarán en la receta
        for reactivo_usado in receta_encontrada['reactivos_utilizados']:
            reactivo_id = reactivo_usado['reactivo_id']
            cantidad_necesaria = reactivo_usado['cantidad_necesaria']
            unidad_medida = reactivo_usado['unidad_medida']

            # Buscar el reactivo correspondiente en la lista de reactivos
            reactivo_encontrado = None
            for reactivo in self.reactivos_json:
                if reactivo['id'] == reactivo_id:
                    reactivo_encontrado = reactivo
                    break

            if not reactivo_encontrado:
                print(f' No se encontró un reactivo con ID {reactivo_id}')
                continue

            # Simular el error de 0.1% a 22.5% (0.001 a 0.225 en valor decimal)
            error = random.uniform(0.001, 0.225)
            cantidad_errada = cantidad_necesaria * error
            
            # Calculamos la cantidad TOTAL que se consumirá de este reactivo
            # (cantidad necesaria + cantidad por el error)
            if reactivo_encontrado['unidad_medida'] == unidad_medida:
                # Misma unidad, no hay conversión
                cantidad_total_consumida = cantidad_necesaria + cantidad_errada
            else:
                # Hay que buscar la conversión
                conversion_encontrada = None
                for conversion in reactivo_encontrado['conversiones_posibles']:
                    if conversion['unidad'] == unidad_medida:
                        conversion_encontrada = conversion
                        break
                if not conversion_encontrada:
                    print(f'ERROR: No se encontró una conversión para la unidad {unidad_medida}.')
                    continue
                # Ajustar la cantidad necesaria a la unidad base del reactivo
                # (por ejemplo, si factor = 1000, significa que 1 kg = 1000 g)
                cantidad_convertida = cantidad_necesaria / conversion_encontrada['factor']
                
                # Asumimos el mismo factor se aplica al 'error' o que ya está medido
                cantidad_errada_convertida = (cantidad_necesaria * error) / conversion_encontrada['factor']
                cantidad_total_consumida = cantidad_convertida + cantidad_errada_convertida

            # Descontar el inventario disponible
            reactivo_encontrado['inventario_disponible'] -= cantidad_total_consumida

            # Calcular el costo parcial = cantidad consumida * costo unitario
            # 'costo' asumimos que está en la misma unidad base que el inventario.
            costo_unitario = reactivo_encontrado.get('costo', 0.0)
            costo_parcial = cantidad_total_consumida * costo_unitario

            # Acumular en el costo total
            costo_total_experimento += costo_parcial

        # Al finalizar, guardamos el costo en el experimento (si así lo deseas) 
        experimento_encontrado['costo_total'] = costo_total_experimento

        print('Experimento realizado exitosamente.')
        print(f'El costo total del experimento es: {costo_total_experimento:.2f}')
