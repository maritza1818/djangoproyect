Discomap - Encuentra tu Discoteca Ideal en Arequipa 🎶🕺
Discomap es una aplicación web en desarrollo que permitirá a los usuarios encontrar las mejores discotecas en Arequipa. Los usuarios podrán consultar información sobre horarios, stock de bebidas, aforo, y calificación de cada discoteca. Las discotecas también podrán registrarse para que los usuarios puedan ver toda esta información.

Estado del Proyecto 🚧
Este proyecto se encuentra actualmente en desarrollo. Hemos implementado la estructura básica tanto del backend (Django) como del frontend (Angular), y estamos trabajando activamente en la integración y en la creación de funcionalidades adicionales.

Características del Proyecto 🌟
Backend (Django)
Autenticación de Usuarios: Los usuarios pueden registrarse e iniciar sesión.
Modelos de Discotecas: Información sobre discotecas, incluyendo horarios, stock de bebidas y aforo.
Consultas JSON: Endpoint para obtener datos en formato JSON.
Frontend (Angular)
Interfaz de Usuario: Los usuarios pueden buscar discotecas y ver sus detalles.
Consultas AJAX: Realiza consultas dinámicas al backend sin recargar la página.
Instalación 🚀
Requisitos Previos:
Python 3.x
Node.js (para Angular)
Django
Angular CLI
Pasos para Instalar:
Clonar el Repositorio:

bash
Copiar código
git clone https://github.com/tu-usuario/discomap.git
Configurar el Backend (Django):

Instala las dependencias de Python:

bash
Copiar código
cd discomap/backend_discomap
pip install -r requirements.txt
Configura la base de datos en settings.py de Django y realiza las migraciones:

bash
Copiar código
python manage.py migrate
Configurar el Frontend (Angular):

Instala las dependencias de Angular:

bash
Copiar código
cd discomap/fronted_discomap
npm install
Ejecuta el servidor de Angular:

bash
Copiar código
ng serve
Ejecutar el Backend:

Inicia el servidor Django:
bash
Copiar código
cd discomap/backend_discomap
python manage.py runserver
¡Accede a la aplicación en http://127.0.0.1:4200 para el frontend y en http://127.0.0.1:8000 para el backend!

Estructura del Proyecto 📁
bash
Copiar código
discomap/
│
├── backend_discomap/         # Backend con Django
│   ├── mysite/               # Proyecto Django
│   ├── manage.py             # Archivo para ejecutar el proyecto Django
│   └── requirements.txt      # Dependencias de Python
│
└── fronted_discomap/         # Frontend con Angular
    ├── discotecas-front/     # Código fuente de Angular
    ├── package.json          # Dependencias de Angular
    └── README.md             # Guía para la instalación del frontend
Ramas y Gestión de Código 🔄
Estructura de Ramas:
main: Rama principal con la última versión estable del proyecto.
feature/: Ramas dedicadas a nuevas funcionalidades o tareas específicas. Cada nueva funcionalidad debe desarrollarse en una rama propia y luego integrarse a main mediante un Pull Request.
Trabajo en Equipo 🤝
El proyecto está siendo desarrollado por un equipo de trabajo, siguiendo las pautas de programación en pareja para asegurar que todos los miembros estén familiarizados con el código.

Contribuciones 📝
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit.
Haz un Pull Request para que tus cambios sean revisados.
Licencia 📄
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
