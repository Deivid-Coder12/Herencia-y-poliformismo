from AnimalesVM import CangrejoVM, CanguroVM, AveVM

class DatosView:
    def __init__(self):
        self.animales = {'1': CangrejoVM, '2': CanguroVM, '3': AveVM}

    def menu(self):
        print("Seleccione una especie:")
        print("1) Cangrejo\n2) Canguro\n3) Ave")
        opc = input("Opción: ").strip()
        if opc not in self.animales:
            print("Opción inválida.")
            return
        edad = input("Edad: ")
        especie = input("Especie: ")
        animal = self.animales[opc](edad, especie)

        while True:
            print("\n1) Caminar\n2) Comer\n3) Guardar\n4) Leer\n5) Actualizar\n6) Eliminar\n7) Salir")
            sel = input("Opción: ").strip()
            if sel == '1':
                animal.caminar()
            elif sel == '2':
                animal.comer()
            elif sel == '3':
                animal.guardar()
            elif sel == '4':
                animal.__class__.leer()
            elif sel == '5':
                id_ = input("ID a actualizar: ")
                nueva_edad = input("Nueva edad (dejar vacío para no cambiar): ")
                nueva_especie = input("Nueva especie (dejar vacío para no cambiar): ")
                animal.__class__.actualizar(id_, nueva_edad or None, nueva_especie or None)
            elif sel == '6':
                animal.__class__.eliminar()
            elif sel == '7':
                break
            else:
                print("Opción inválida.")
