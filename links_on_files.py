Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. 

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.

import requests

start = 'https://stepic.org/media/attachments/course67/3.6.3/'
file = '699991.txt'

while file:
    print(file)
    name = requests.get(start + file)
    file = None \
        if name.text.startswith('We') \
        else name.text
    
with open('konec.txt' 'w') as konec:
    konec.write(name.text)
    konec.close()
    
    # Задача из курса по Python'у на https://stepik.org
