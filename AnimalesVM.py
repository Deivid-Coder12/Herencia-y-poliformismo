from Observable import Observable
import firebase_admin
from firebase_admin import credentials, db

# Inicialización de Firebase
cred = credentials.Certificate('C:/Users/HP/OneDrive/Documentos/POO/Herencia y poliformismo/herencia-y-poliformismo-firebase-adminsdk-fbsvc-62453e6991.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://herencia-y-poliformismo-default-rtdb.firebaseio.com/'
})

class AnimalVM:
    def __init__(self, edad, especie):
        self.edad = Observable(edad)
        self.especie = Observable(especie)
    
    def caminar(self):
        print("El animal está caminando")
    
    def comer(self):
        print("El animal está comiendo")
    
    def guardar(self):
        # Obtener el nombre de la categoría basado en el nombre de la clase
        categoria = self.__class__.__name__.lower().replace('vm', '')
        tipo = {
            'edad': self.edad.value,
            'especie': self.especie.value
        }
        db.reference(f'animales/{categoria}').push(tipo)
        print(f"{categoria.capitalize()} guardado correctamente en Firebase.")
    
    @classmethod
    def leer(cls, tipo=None):
        select_categoria = input("Seleccione la categoría a leer:\n1) Cangrejo\n2) Canguro\n3) Ave\nOpción: ").strip()
        
        if select_categoria == '1':
            tipo = 'cangrejo'
        elif select_categoria == '2':
            tipo = 'canguro'
        elif select_categoria == '3':
            tipo = 'ave'
        else:
            print("Opción inválida.")
            return
        
        datos = db.reference(f'animales/{tipo}').get()
        
        if datos is None or len(datos) == 0:
            print(f"No hay datos disponibles para {tipo}.")
            return
        
        print(f"Datos de {tipo.capitalize()}:")
        for key, value in datos.items():
            print(f"ID: {key}, Edad: {value['edad']}, Especie: {value['especie']}")
    
    @classmethod
    def eliminar(cls):
        print("Elija la categoría a eliminar")
        categoria = input("1) Cangrejo\n2) Canguro\n3) Ave\nOpción: ").strip()
        
        if categoria == '1':
            tipo = 'cangrejo'
        elif categoria == '2':
            tipo = 'canguro'
        elif categoria == '3':
            tipo = 'ave'
        else:
            print("Opción inválida.")
            return
        
        db.reference(f'animales/{tipo}').delete()
        print(f"Datos de {tipo} eliminados correctamente.")
    
    @classmethod
    def actualizar(cls, id_dato, nueva_edad=None, nueva_especie=None):
        tipo = cls.__name__.lower().replace('vm', '')
        ref = db.reference(f"animales/{tipo}/{id_dato}")
        data = {}
        
        if nueva_edad:
            data['edad'] = nueva_edad
        if nueva_especie:
            data['especie'] = nueva_especie
        
        ref.update(data)
        print(f"{tipo} con ID {id_dato} actualizado correctamente.")

class CangrejoVM(AnimalVM):
    def caminar(self):
        print("El cangrejo avanza caminando de lado")
    
    def comer(self):
        print("El cangrejo está comiendo algas")

class CanguroVM(AnimalVM):
    def caminar(self):
        print("El canguro está saltando")
    
    def comer(self):
        print("El canguro está comiendo pasto")

class AveVM(AnimalVM):
    def caminar(self):
        print("El ave está volando")
    
    def comer(self):
        print("El ave está comiendo semillas")