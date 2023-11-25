# -*- coding: utf-8 -*-
import requests
import bs4
import easygui
import os

url = 'https://rustxt.ru/chast-rechi'
input_file = easygui.fileopenbox(filetypes=["*.txt"])
with open(input_file, 'r', encoding='utf-8') as word_file:
    with open('result_pos.txt', 'w+', encoding='utf-8') as result_file:
        f = word_file.read()
        count = 0
        for word in f.split('\n'):
            count += 1
            print('\r[+] Слов обработано: ' + str(count), end='')
            data = {'text': word, 'method': 'search', 'utm': '', 'ReturnSrcSearch': 1}
            response = requests.post(url, data=data)
            src = response.content.decode('utf-8')
            soup = bs4.BeautifulSoup(src, features='lxml')
            pos = soup.find_all('span', {'class': 'text-uppercase'})
            if len(pos) > 0:
                result_file.write(str(pos[0]).split('<')[1][28:].lower() + ';' + word + '\n')
            else:
                result_file.write('Не смог определить(' + ';' + word + '\n')
print('\n[*] Все готово!')
os.system('result_pos.txt')