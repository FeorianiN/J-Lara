import os
import re
import json


def configuration_loading():
    #  configuration-info about location of data-files

    line = ['']
    error_code = 0
    disposition_of_data_file = ""

    #  load info from config-file
    try:
        f = open('Config.md')
        line = f.readlines()

        #  parse file
        line[0] = re.sub('\n', '', line[0])
        disposition_of_data_file = line[0]

        f.close()
    except:
        error_code = 4

    return disposition_of_data_file, error_code


def reading_from_the_data_file():

    error_code = 0

    #  load path to the data-file from config-info
    disposition_of_data_file, error_code = configuration_loading()

    if error_code == 0:
        #  load information
        try:
            data_from_the_file = json.load(open(disposition_of_data_file))
        except:
            error_code = 2
            data_from_the_file = dict()

    return data_from_the_file, error_code


def writing_to_the_data_file(wish):

    error_code = 0

    #  load config-info
    disposition_of_data_file, error_code = configuration_loading()

    if error_code == 0:
        #  load old information
        data_from_the_file, error_code = reading_from_the_data_file()

        #  continue working if all were right
        if error_code == 0:

            #  merge new and old information
            data_from_the_file["Future"].append({"wish": wish})

            #  rewrite all the data
            try:
                with open(disposition_of_data_file, 'w') as file:
                    json.dump(data_from_the_file, file, indent=2, ensure_ascii=False)
            except:
                error_code = 2

    return error_code
