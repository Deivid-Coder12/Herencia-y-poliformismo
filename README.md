Sistema de Gestión de Animales con Firebase
Proyecto de programación orientada a objetos que implementa un sistema de gestión de animales (cangrejos, canguros y aves) con persistencia de datos en Firebase Realtime Database. El proyecto utiliza el patrón de diseño MVVM (Model-View-ViewModel) y el patrón Observable para la gestión de datos reactivos.

📋 Características
✅ Gestión de tres tipos de animales: Cangrejo, Canguro y Ave

✅ Operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar)

✅ Persistencia de datos en Firebase Realtime Database

✅ Patrón Observable para gestión reactiva de datos

✅ Arquitectura MVVM para separación de responsabilidades

✅ Herencia y polimorfismo en la implementación de animales

✅ Interfaz de línea de comandos interactiva

🛠️ Tecnologías Utilizadas
Python 3.x

Firebase Admin SDK - Para la integración con Firebase Realtime Database

Patrón MVVM - Arquitectura del proyecto

Patrón Observable - Para gestión de estado reactivo

📁 Estructura del Proyecto
text
proyecto-animales/
│
├── main.py                  # Punto de entrada de la aplicación
├── DatosView.py            # Capa de vista (interfaz de usuario)
├── AnimalesVM.py           # ViewModels y lógica de negocio
├── Observable.py           # Implementación del patrón Observable
├── README.md               # Este archivo
└── herencia-y-poliformismo-firebase-adminsdk-*.json  # Credenciales de Firebase
🚀 Instalación
Prerrequisitos
Python 3.7 o superior instalado

Una cuenta de Firebase con un proyecto creado

Credenciales de Firebase Admin SDK

Pasos de Instalación
Clonar o descargar el proyecto

bash
git clone <url-del-repositorio>
cd proyecto-animales
Instalar dependencias

bash
pip install firebase-admin
Configurar Firebase

a. Ve a la Consola de Firebase

b. Crea un nuevo proyecto o selecciona uno existente

c. Ve a Configuración del proyecto → Cuentas de servicio

d. Haz clic en Generar nueva clave privada para descargar el archivo JSON

e. Guarda el archivo JSON en el directorio del proyecto

f. Actualiza la ruta en AnimalesVM.py:

python
cred = credentials.Certificate('RUTA/A/TU/ARCHIVO/firebase-credentials.json')
Configurar la URL de la base de datos

En AnimalesVM.py, actualiza la URL de tu base de datos:

python
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://TU-PROYECTO.firebaseio.com/'
})
💻 Uso
Ejecutar la aplicación
bash
python main.py
Menú Principal
Al iniciar la aplicación, verás el siguiente menú:

text
Seleccione una especie:
1) Cangrejo
2) Canguro
3) Ave
Opción:
Después de seleccionar una especie e ingresar edad y nombre, aparecerá el menú de operaciones:

text
1) Caminar
2) Comer
3) Guardar
4) Leer
5) Actualizar
6) Eliminar
7) Salir
Funcionalidades
1. Caminar
Muestra el comportamiento específico de cada animal al caminar:

Cangrejo: Camina de lado

Canguro: Salta

Ave: Vuela

2. Comer
Muestra el comportamiento específico de cada animal al comer:

Cangrejo: Come algas

Canguro: Come pasto

Ave: Come semillas

3. Guardar
Guarda el animal actual en Firebase bajo la categoría correspondiente.

4. Leer
Lee y muestra todos los animales de una categoría específica desde Firebase.

5. Actualizar
Actualiza los datos de un animal específico en Firebase usando su ID.

6. Eliminar
Elimina todos los animales de una categoría desde Firebase.

7. Salir
Cierra la aplicación.

📚 Arquitectura del Proyecto
Patrón MVVM
El proyecto implementa el patrón MVVM (Model-View-ViewModel):

View (DatosView.py): Interfaz de usuario que maneja la interacción con el usuario

ViewModel (AnimalesVM.py): Lógica de negocio y comunicación con Firebase

Model (Observable.py): Gestión del estado de los datos

Jerarquía de Clases
text
AnimalVM (clase base)
│
├── CangrejoVM
├── CanguroVM
└── AveVM
Patrón Observable
La clase Observable implementa el patrón Observer, permitiendo:

Suscripción a cambios de valor

Notificación automática a los observadores

Gestión reactiva del estado

🔧 Descripción de los Archivos
main.py
Punto de entrada de la aplicación. Inicializa la vista y ejecuta el menú principal.

DatosView.py
Maneja la interfaz de usuario y la interacción con el usuario a través de la consola.

AnimalesVM.py
Contiene:

Inicialización de Firebase

Clase base AnimalVM con métodos CRUD

Clases derivadas: CangrejoVM, CanguroVM, AveVM

Implementación de herencia y polimorfismo

Observable.py
Implementa el patrón Observable para la gestión reactiva de datos con:

Sistema de suscripción

Notificación de cambios

Getters y setters personalizados

🔐 Seguridad
⚠️ Importante:

NO subas el archivo de credenciales de Firebase a repositorios públicos

Añade *.json a tu .gitignore

Considera usar variables de entorno para datos sensibles en producción

Ejemplo de .gitignore:

text
# Firebase credentials
*-firebase-adminsdk-*.json
firebase-credentials.json

# Python
__pycache__/
*.py[cod]
*$py.class
.env
📊 Estructura de Datos en Firebase
Los datos se organizan en Firebase de la siguiente manera:

text
animales/
├── cangrejo/
│   ├── {id1}/
│   │   ├── edad: "3"
│   │   └── especie: "Rojo"
│   └── {id2}/
│       ├── edad: "5"
│       └── especie: "Azul"
├── canguro/
│   └── {id1}/
│       ├── edad: "7"
│       └── especie: "Gigante"
└── ave/
    └── {id1}/
        ├── edad: "2"
        └── especie: "Águila"
