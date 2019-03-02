#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import Json
import Logic
import Output

def main(wish):

    #  variable for checking type of errors
    error_code = 0

    try:
        #  load information from json-file
        all_data = dict()
        all_data = Json.reading_from_the_file()
    except:
        error_code = 2

    if error_code == 0:
        error_code = Logic.core(all_data, wish)


if __name__ == '__main__':

    wish = ""
    main(wish)
