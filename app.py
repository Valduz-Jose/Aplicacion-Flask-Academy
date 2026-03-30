import os
from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db, migrate
import models

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de la Base de Datos
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Construcción de la URI de conexión: mysql+pymysql://usuario:password@host:puerto/nombre_bd
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Inicializar extensiones con la app
db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)