from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializamos las extensiones sin el objeto 'app'
db = SQLAlchemy()
migrate = Migrate()