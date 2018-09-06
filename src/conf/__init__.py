# création d'un path pour les fichiers de conf
#
#DominiqueHathi
#11/12/2017
#version 1.0

import os

def get_current_dir(current_file):
    return os.path.dirname(os.path.abspath(current_file))

def get_data_dir(current_file):
    return os.path.join(get_current_dir(current_file), "")

DATA_DIR = get_data_dir(__file__)
