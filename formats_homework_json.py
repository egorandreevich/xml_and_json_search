from pprint import pprint
import json
with open('./newsafr.json', encoding = 'utf-8_sig') as datafile:
    json_data = json.load(datafile)

for value in json_data.values():
    value_dict = value

channel_dict = value_dict['channel']
items_list = channel_dict['items']
general_list = []

def getDescriptions(custom_list):
    for item in custom_list:
        if 'description' in item:
            general_list.append(item['description'].split())

getDescriptions(items_list)

more_than_six_list = []

def checkIfMoreThanSix():
    for word in general_list[0]:
        if len(word) >= 6:
            more_than_six_list.append(word)

checkIfMoreThanSix()

def sortingTopTen():
    sorted_word_list = sorted(more_than_six_list, key=len, reverse=True)
    print('ТОП 10 самых длинных слов в новостях про Африку:')
    pprint(sorted_word_list[0:10])

sortingTopTen()
