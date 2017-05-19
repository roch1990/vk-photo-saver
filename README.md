vk.com photo saver
==================

### What is it?

Small script for saving vk photos.

### How it works

At first for list of albums:
- Send a querry to api.vk
- Read api.vk JSON answer

Then download all photos from every album

### What i need to start?
- python 3.5
- pip3

### How to run

- Run `pip3 install -r requirements`
- Fill config.py with CLIENT_ID (your app id) and USER_ID (id of user, that hold photos)
- Run __init__.py
- Copy connection string to your browser and get token
- Fill config.py API_TOKEN with token :)
- Wait for result

### Troubleshooting

If you get a message with description "too many requests per second" - wait for a minute and try again.
If you want to open a issue - add a stdout and vksaver.log.

### To do :

- multiprocessing
- restart, after crashing from last step of previous itteration
- automatic token retrieving

### Что это ?

Не большой скрипт для загрузки фото с vk.com

### Как это работает?

- Парсятся альбомы пользователя
- Парсятся фото в каждом альбоме
- Составляется JSON вида `{'альбом' : ['список', 'фотографий']}`
- Происходит загрузка фотографий в папку `./out`

Общение с vk.com происходит посредством api.vk

### Что мне нужно для запуска скрипта?
- python 3.5
- pip3

### Как запустить?

- Запустить `pip3 install -r requirements.txt`
- Получить id приложения на страничке девелопера vk.com
- Записать в `CLIENT_ID` модуля `config.py` id приложения
- Записать в `USER_ID` модуля `config.py` id пользователя (фото которого вам нужны)
- Запускайте `__init__.py`
- Скопируйте строку подключения из консоли в адресную строку браузера и перейдите по ней
- Скопируйте токен из полученной адресной строки в `API_TOKEN` модуля `config.py`
- Введите `Y` нажмите `Enter`

### Troubleshooting

- Если у Вас не запустился скрипт с первого раза - запустите его повторно, возможно API_TOKEN не подхватился.
- Если скрипт крашнулся во время выполнения - скорее всего vk.com отклонило запрос с ошибкой `to many requests per second`.
Попробуйте запустить скрипт снова

- Если хотите открыть issue - прикладывайте вывод vksaver.log и stdout.

- Протещено на Ubuntu 16.04 и Windows7

### Планы :

- многопоточная загрузка
- перезапуск после краша скрипта, с последнего шага
- автоматическое получение токена