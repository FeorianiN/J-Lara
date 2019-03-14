import os
import re


def core(all_data, wish):

    number_of_answer = 0
    error_code = 0
    result = False
    accuracy = []
    answer = ""

    #  parser of the wish and data, which return such processed data as:
    #  frequency of including wish-words in data-words
    #  and len of the every data-string for calculating accuracy of every result
    frequency_of_coincidences, len_of_the_json_string, error_code = data_parser(all_data, wish)

    if error_code == 0:

        #  calculating accuracy-data in case of
        #  wish-words in data-words frequency of includes
        accuracy, result, error_code = frequency_processor(frequency_of_coincidences, len_of_the_json_string)

        if error_code == 0 and result == True:

            #  searching for the best answer for the wish
            number_of_the_best_answer, error_code = accuracy_processor(accuracy)

            #  searching for the answer on [number_of_the_best_answer] position in all information
            if error_code == 0:
                answer = all_data["JL"][number_of_the_best_answer]["answer"]
            else:
                error_code = 3

    return answer, result, error_code


def data_parser(all_data, wish):

    error_code = 0

    #  wish-string parsing to words
    help_string = wish.lower()
    words_in_wish = help_string.split()

    #  variables for check, what is the frequency
    #  of including wish-words in data-words
    frequency_of_coincidences = []
    len_of_the_json_string = []
    temp_frequency = 0
    temp_len = 0

    try:
        #  start to finding coincidences in data...

        #  data-string parsing to words
        for i in range(len(list(all_data["JL"]))):
            processing_string = all_data["JL"][i]["wish"].lower()
            processing_words = processing_string.split()

            #  searching in current data-string...
            for j in range(len(list(processing_words))):
                temp_len = temp_len + 1

                #  searching in current data-string wish-words
                for k in range(len(list(words_in_wish))):
                    if processing_words[j] == words_in_wish[k]:
                        temp_frequency = temp_frequency + 1

            #  save temp frequency-info and len-info
            frequency_of_coincidences.append(temp_frequency)
            len_of_the_json_string.append(temp_len)

            temp_frequency = 0
            temp_len = 0
    except:
        error_code = 3

    return frequency_of_coincidences, len_of_the_json_string, error_code


def frequency_processor(frequency_of_coincidences, len_of_the_json_string):

    error_code = 0
    result = False
    accuracy = []

    #  calculating accuracy for every data-line
    for i in range(len(list(frequency_of_coincidences))):
        temp_acc = 0
        temp_acc = frequency_of_coincidences[i] / len_of_the_json_string[i]
        accuracy.append(temp_acc)

    for j in range(len(list(accuracy))):

        #  bottom limit for accuracy of the answer(limit * 100%)
        limit = 0.1
        if accuracy[j] > limit:
            result = True

    return accuracy, result, error_code


def accuracy_processor(accuracy):

    error_code = 0

    #  searching for an answer with max accuracy
    max_accuracy_number = 0
    for i in range(len(list(accuracy))):
        if (accuracy[i] > 0) and (accuracy[i] > accuracy[max_accuracy_number]):
            max_accuracy_number = i

    number_of_the_best_answer = max_accuracy_number

    return number_of_the_best_answer, error_code
