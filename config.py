import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    ''' This values should be set in the enviorament to can get them and not have them in the code'''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = os.environ.get('MYSQL_DB')

    '''
    Just to remember:
    set VARIABLE_NAME=value      #to set a variable in the enviorament
    setx VARIABLE_NAME value     #return a confirmation that the variable is saved

    '''

    