import os
import re
import json


def reading_from_the_file():

    #  load path to the data-file from config-info
    disposition_of_file = "JL.json"

    #  load information
    try:
        data_from_the_file = json.load(open(disposition_of_file))
    except:
        data_from_the_file = dict()

    return data_from_the_file
