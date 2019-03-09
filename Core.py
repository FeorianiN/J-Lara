#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import Tk
import Json
import Logic
import Output


def main(wish):

    #  variable for checking type of errors
    error_code = 0

    try:
        #  load information from json-file
        all_data = dict()
        all_data, error_code = Json.reading_from_the_data_file()
    except:
        error_code = 2

    if error_code == 0:
        result, error_code = Logic.core(all_data, wish)

    if result == True:

        # show answer to user
        Output.positive_output()

    # if answer wasn't given...
    elif result == False:

        # show sorry-message to user
        Output.negative_output()

        # write wish to the list for future answers
        error_code = Json.writing_to_the_data_file(wish)

    Tk.main()

    return error_code


if __name__ == '__main__':

    wish = "Tell me a story"
    main(wish)
