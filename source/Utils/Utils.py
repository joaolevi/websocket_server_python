from os import path, makedirs
from inspect import getfile, currentframe
from logging import basicConfig, getLogger, DEBUG

def get_main_directory():
    return (path.dirname(path.abspath(getfile(currentframe()))))

def start_log(class_name):
    maindirectory = get_main_directory()
    directory = maindirectory + '/log'
    if (not path.exists(directory)):
        makedirs(directory)

    basicConfig(filename="../log/Event"+ class_name + ".log", format='%(asctime)s %(message)s', filemode='w')
    EventWriter = getLogger()
    EventWriter.setLevel(DEBUG)
    return EventWriter