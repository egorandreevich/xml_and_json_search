from pprint import pprint
import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")

tree = ET.parse('./newsafr.xml', parser=parser)
titles = []

root = tree.getroot()
title = root.find('channel/title')
items = root.findall('channel/item')

general_list = []
more_than_six_list = []

def get_descriptions(custom_list):
    for xmli in custom_list:
        general_list.append(xmli.find('description').text.split())


def check_if_more_than_six():
    for word in one_list:
        if len(word) >= 6 and word.lower() not in more_than_six_list:
            more_than_six_list.append(word.lower())


def sorting_top_ten():
    sorted_word_list = sorted(more_than_six_list, key=len, reverse=True)
    print('ТОП 10 самых длинных слов в новостях про Африку:')
    pprint(sorted_word_list[0:10])

if __name__ == '__main__':
    get_descriptions(items)

    one_list = [item for sublist in general_list for item in sublist]

    check_if_more_than_six()
    sorting_top_ten()