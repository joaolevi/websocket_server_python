from os import path, makedirs
from inspect import getfile, currentframe
from logging import basicConfig, getLogger, DEBUG
from yaml import safe_load

def get_main_directory():
    return (path.dirname(path.abspath(getfile(currentframe()))))

def read_config_db_file(maindirectory):
    try:
        with open(maindirectory + "config/DBConfig.yaml", 'r') as fileconfig:
            config = safe_load(fileconfig)
    except Exception as e:   
        config = {'login'   : 'postgres', 
                  'password': '1234',
                  'ip'      : 'localhost',
                  'port'    : '5432'}
    return config

def start_log(class_name, maindirectory):
    # directory = maindirectory + '/log'
    # if (not path.exists(directory)):
    #     makedirs(directory)

    basicConfig(filename="../log/Event"+ class_name + ".log", format='%(asctime)s %(message)s', filemode='w')
    EventWriter = getLogger()
    EventWriter.setLevel(DEBUG)
    return EventWriter