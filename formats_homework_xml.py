from pprint import pprint
import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")

tree = ET.parse('./newsafr.xml', parser=parser)
titles = []

root = tree.getroot()
title = root.find('channel/title')
items = root.findall('channel/item')

general_list = []
top_words_list = []

def get_descriptions(custom_list):
    for xmli in custom_list:
        general_list.extend(xmli.find('description').text.split())

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
    get_descriptions(items)
    top_words(general_list)
    top_ten(top_words_list)
