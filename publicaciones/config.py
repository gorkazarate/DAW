class Config():

    DEBUG = True
    TESTING = True 
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/serviweb'  # Asignar el valor
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'AIzaSyA5uU19N9Y44HLnNh9OAhZeuQrrbm6ljZE'
    DEBUG = True
    TESTING = True