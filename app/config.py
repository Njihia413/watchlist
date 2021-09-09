#Where we will store our app configurations
from re import DEBUG


class Config:
    '''
    Parent configuration class with general configuration settings
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: Parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: Parent confuguration class with general configuration settings
    '''
    DEBUG = True