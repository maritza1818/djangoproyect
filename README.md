# Discomap - Encuentra tu Discoteca Ideal en Arequipa 🎶🕺

**Discomap** es una aplicación web en desarrollo que permitirá a los usuarios encontrar las mejores discotecas en Arequipa. Los usuarios podrán consultar información sobre horarios, stock de bebidas, aforo, y calificación de cada discoteca. Las discotecas también podrán registrarse para que los usuarios puedan ver toda esta información.

## Estado del Proyecto 🚧
Este proyecto se encuentra actualmente en desarrollo. Hemos implementado la estructura básica tanto del **backend (Django)** como del **frontend (Angular)**, y estamos trabajando activamente en la integración y en la creación de funcionalidades adicionales.

## Características del Proyecto 🌟

### Backend (Django)
- **Autenticación de Usuarios**: Los usuarios pueden registrarse e iniciar sesión.
- **Modelos de Discotecas**: Información sobre discotecas, incluyendo horarios, stock de bebidas y aforo.
- **Consultas JSON**: Endpoint para obtener datos en formato JSON.

### Frontend (Angular)
- **Interfaz de Usuario**: Los usuarios pueden buscar discotecas y ver sus detalles.
- **Consultas AJAX**: Realiza consultas dinámicas al backend sin recargar la página.

## Instalación 🚀

### Requisitos Previos:
- **Python 3.x**
- **Node.js** (para Angular)
- **Django**
- **Angular CLI**

### Pasos para Instalar:

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/discomap.git

### Configurar el Backend (Django):

1. **Instala las dependencias de Python:**

   ```bash
   cd discomap/backend_discomap
   pip install -r requirements.txt
   
2. **Configura la base de datos en settings.py de Django y realiza las migraciones:**

   ```bash
     python manage.py migrate

### Configurar el Frontend (Angular):
1.**Instala las dependencias de Angular:**
   ```bash
cd discomap/fronted_discomap
npm install

