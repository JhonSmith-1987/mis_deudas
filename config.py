class Config:
    SECRET_KEY = 'harnoldoratinina'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'mi_presupuesto'


config = {
    'development': DevelopmentConfig
}

