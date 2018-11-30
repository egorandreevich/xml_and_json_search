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

def getDescriptions(custom_list):
    for xmli in custom_list:
        general_list.append(xmli.find('description').text.split())

getDescriptions(items)

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