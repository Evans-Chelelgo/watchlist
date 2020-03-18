import os

class Config:

    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLAlCHEMY_DATABASE_URI ='postgresql+psycopg2://ubunifu:evans1234@localhost/watchlist'


class ProdConfig(Config):
    '''
    production configuration child class

    args:
         Config:
            The parent configuration class with general configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child clapp.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('postgresql+psycopg2://ubunifu:evans1234@localhost/watchlist')ass

    args:
         Config:
            The parent configuration class with general configuration settings
    '''

    DEBUG = True       

config_options = {
'production': ProdConfig,    
'development': DevConfig
    } 