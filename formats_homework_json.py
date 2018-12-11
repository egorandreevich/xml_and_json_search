from pprint import pprint
import json

with open('./newsafr.json', encoding = 'utf-8_sig') as datafile:
    json_data = json.load(datafile)

for value in json_data.values():
    value_dict = value

general_list = []
more_than_six_list = []

def get_descriptions(custom_list):
    for item in custom_list:
        if 'description' in item:
            general_list.append(item['description'].split())

def check_if_more_than_six():
    for word in one_list:
        if len(word) >= 6 and word.lower() not in more_than_six_list:
            more_than_six_list.append(word.lower())

def sorting_top_ten():
    sorted_word_list = sorted(more_than_six_list, key=len, reverse=True)
    print('ТОП 10 самых длинных слов в новостях про Африку:')
    pprint(sorted_word_list[0:10])


if __name__ == '__main__':
    get_descriptions(value_dict['channel']['items'])

    one_list = [item for sublist in general_list for item in sublist]

    check_if_more_than_six()
    sorting_top_ten()
