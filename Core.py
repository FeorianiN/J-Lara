#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import Tk
import Json
import Logic
import Output
import platform
import subprocess


def main(wish):

    #  variable for checking type of errors
    error_code = 0

    answer = ""
    result = False
    all_data = dict()

    try:
        #  load information from json-file
        all_data, error_code = Json.reading_from_the_data_file()
    except:
        error_code = 2

    if error_code == 0:
        answer, result, error_code = Logic.core(all_data, wish)

    if result == True:

        # management command: switch off
        if answer == "Ok, bye":
            subprocess.call(["shutdown", "/s"])

        # management command: restart
        elif answer == "Ok, see you soon":
            subprocess.call(["shutdown", "/r"])

        elif answer == "Ok, here it is":
            if platform.system() == "Windows":
                os.startfile("C:")
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", "C:"])
            else:
                subprocess.Popen(["xdg-open", "C:"])

        else:
            # show answer to user
            Output.positive_output(answer)

    # if answer wasn't given...
    elif result == False:

        # show sorry-message to user
        Output.negative_output()

        # write wish to the list for future answers
        error_code = Json.writing_to_the_data_file(wish)

    return answer, result, error_code


if __name__ == '__main__':

    Tk.main()
