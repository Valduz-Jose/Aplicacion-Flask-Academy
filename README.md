# 🎓 Flask Academy - Sistema de Gestión de Cursos

**Flask Academy** es una aplicación web profesional desarrollada con **Python** y **Flask** para la administración de cursos académicos. Este proyecto representa una evolución técnica significativa, implementando una arquitectura de capas y el uso de un **ORM** para una gestión de datos robusta y escalable.

## 🌟 Características Destacadas

* **Arquitectura de Servicios:** Implementación de una capa de servicios (`CursoService`) para separar la lógica de negocio de las rutas de Flask (Controladores).
* **SQLAlchemy ORM:** Uso de Mapeo Objeto-Relacional para interactuar con MySQL, permitiendo un código más limpio y orientado a objetos.
* **Gestión de Migraciones:** Integración con **Flask-Migrate** (Alembic) para el control de versiones del esquema de la base de datos.
* **Seguridad con Variables de Entorno:** Configuración protegida mediante el uso de archivos `.env` y la librería `python-dotenv`.
* **Formularios Avanzados:** Uso de `Flask-WTF` para validaciones de servidor y protección contra ataques CSRF.
* **Interfaz Dinámica:** Dashboard responsivo construido con **Bootstrap 5** y renderizado mediante el motor de plantillas **Jinja2**.

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.x, Flask.
* **Base de Datos:** MySQL.
* **Persistencia (ORM):** Flask-SQLAlchemy.
* **Frontend:** HTML5, Jinja2, Bootstrap 5.
* **Herramientas:** Flask-Migrate, Flask-WTF, PyMySQL.

## 📋 Estructura del Proyecto

* `app.py`: Punto de entrada de la aplicación y configuración del servidor.
* `models.py`: Definición de los modelos de datos (Tablas de base de datos).
* `services/curso_service.py`: Lógica de negocio y operaciones de datos.
* `forms.py`: Definición y validación de formularios web.
* `extensions.py`: Inicialización de extensiones (DB, Migrate).
* `.env`: Configuración de credenciales de acceso (No incluido por seguridad).

## 🔧 Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Valduz-Jose/Flask-Academy.git](https://github.com/Valduz-Jose/Flask-Academy.git)
    cd Flask-Academy
    ```

2.  **Configurar variables de entorno:**
    Crea un archivo `.env` en la raíz y añade tus credenciales:
    ```text
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=flask_academy_db
    SECRET_KEY=una_clave_secreta_aleatoria
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Preparar la Base de Datos:**
    ```bash
    flask db init
    flask db migrate -m "Migración inicial"
    flask db upgrade
    ```

5.  **Ejecutar:**
    ```bash
    python app.py
    ```
<img width="1659" height="775" alt="Captura de pantalla 2026-03-30 115902" src="https://github.com/user-attachments/assets/ef33183b-ad33-4965-9eec-129951d4fd54" />
<img width="1727" height="705" alt="Captura de pantalla 2026-03-30 115854" src="https://github.com/user-attachments/assets/716fb3b7-17b7-4b45-9da8-8deaba8f3d13" />
<img width="885" height="610" alt="Captura de pantalla 2026-03-30 115835" src="https://github.com/user-attachments/assets/d711cac1-8345-45b7-99a8-9761cd75a0f0" />
<img width="1703" height="804" alt="Captura de pantalla 2026-03-30 115827" src="https://github.com/user-attachments/assets/a4bbc8a9-4c57-431f-b3a6-6244fce3b4ae" />
<img width="961" height="645" alt="Captura de pantalla 2026-03-30 115818" src="https://github.com/user-attachments/assets/2a95a494-f43b-48f7-b516-3878e2a76f53" />
<img width="1726" height="688" alt="Captura de pantalla 2026-03-30 115748" src="https://github.com/user-attachments/assets/78de7851-aacb-483c-845d-06fdd2d8b901" />

---
Desarrollado por **Jose Valduz** | 2026
