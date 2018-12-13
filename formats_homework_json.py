from pprint import pprint
import json
from pprint import pprint

with open('./newsafr.json', encoding = 'utf-8_sig') as datafile:
    json_data = json.load(datafile)

for value in json_data.values():
    value_dict = value

general_list = []
top_words_list = []

def get_descriptions(custom_list):
    for item in custom_list:
        if 'description' in item:
            general_list.extend(item['description'].split())

def top_words(custom_list): #Получаем в виде словаря частотность слов, которые состоят более чем из 6 символов
    super_dic = {}
    super_list = []
    for item in custom_list:
        item = item.lower()
        if item not in super_dic.keys() and len(item) > 6:
            super_dic[item] = 1
        elif item in super_dic.keys() and len(item) > 6:
            super_dic[item] += 1
    for key, value in super_dic.items(): #Организуем в кортежи
        top_words_list.append((key, value))

def top_ten(custom_list): #Сортируем по частотности и выделяем топ-10
    top_ten_list = sorted(custom_list, key=lambda x: x[1], reverse=True)
    pprint(top_ten_list[0:10])
    return top_ten_list


if __name__ == '__main__':
    get_descriptions(value_dict['channel']['items'])
    top_words(general_list)
    top_ten(top_words_list)
