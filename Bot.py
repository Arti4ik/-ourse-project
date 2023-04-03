import telebot             # библиотека для  создания Telegram Bota
import requests            # библиотека для
import random                # импортируем рандом
from config import token      # импортируем токен Telegram Bota из файла confif.py
from telebot import types           # из библиотеки telebot  импортируем types(чтобы добавлять кнопки в Bot)
from bs4 import BeautifulSoup as b     # библиотека для парсинка страниц в браузере


# Короткие анекдоты
URL_1 = "https://anekdoty.ru/korotkie/"   # ссылка на страницу с короткими анекдотами
def parser_1(url):                        # функция выполняющая парсинг(сбор данных) с заданной страницы
    r = requests.get(url=url)             # сохраняем get запрос сделанный с помощью библиотеки requests, в переменную
    soup_1 = b(r.text, "html.parser")     # указываем , чтобы парсер выводил текстовые данные
    anekdots_1 = soup_1.find_all("div", class_="holder")   # указываем тег и классы от куда будут браться все текстовые данные с заданной страницы
    return [i.text.split('#')[-2] for i in anekdots_1]     # вызываем функцию,где собранны все данные в список
listing_1 = parser_1(URL_1)         # сохраняем в переменную ,данные в списке
random.shuffle(listing_1)           # указываем чтобы данные в списке были в рандомной последовательности

# Анекдоты про программистов
URL_2 = "https://anekdoty.ru/pro-programmistov/"
def parser_2(url):               # функция выполняющая парсинг с заданной страницы Анекдоты про программистов
    r = requests.get(url)
    soup_2 = b(r.text, "html.parser")
    anekdots_2 = soup_2.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_2]
listing_2 = parser_2(URL_2)
random.shuffle(listing_2)

# Анекдоты для взрослых
URL_3 = "https://anekdoty.ru/pro-vzroslyh/"
def parser_3(url):                # функция выполняющая парсинг с заданной страницы Анекдоты для взрослых
    r = requests.get(url)
    soup_3 = b(r.text, "html.parser")
    anekdots_3 = soup_3.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_3]
listing_3 = parser_3(URL_3)
random.shuffle(listing_3)

# Анекдоты для детей
URL_4 = "https://anekdoty.ru/detskie/"
def parser_4(url):                # функция выполняющая парсинг с заданной страницы Анекдоты для детей
    r = requests.get(url)
    soup_4 = b(r.text, "html.parser")
    anekdots_4 = soup_4.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_4]
listing_4 = parser_4(URL_4)
random.shuffle(listing_4)

# Анекдоты про чёрный юмор
URL_5 = "https://anekdoty.ru/detskie/"
def parser_5(url):                # функция выполняющая парсинг с заданной страницы Анекдоты про чёрный юмор
    r = requests.get(url)
    soup_5 = b(r.text, "html.parser")
    anekdots_5 = soup_5.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_5]
listing_5 = parser_5(URL_5)
random.shuffle(listing_5)

# Анекдоты про Наркоманов
URL_6 = "https://anekdoty.ru/pro-narkomanov/"
def parser_6(url):                 # функция выполняющая парсинг с заданной страницы Анекдоты про Наркоманов
    r = requests.get(url)
    soup_6 = b(r.text, "html.parser")
    anekdots_6 = soup_6.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_6]
listing_6 = parser_6(URL_6)
random.shuffle(listing_6)

bot = telebot.TeleBot(token)         # Создаем экземпляр бота

@bot.message_handler(commands=["start"])     # Функция, обрабатывающая команду /start
def welcome(message):
    bot.send_message(message.chat.id, ' Привет,{0.first_name}!\nЯ - <b>{1.first_name}</b>, '
                                      '🤖 созданный чтобы тебе поднять настроение'.format(message.from_user, bot.get_me()),parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Короткие")
    item2 = types.KeyboardButton("Про программистов")
    item3 = types.KeyboardButton("Для взрослых")
    item4 = types.KeyboardButton("Для детей")
    item5 = types.KeyboardButton("Чёрный юмор")
    item6 = types.KeyboardButton("Про наркоманов")
    markup.add(item1,item2,item3,item4,item5,item6)      # добавляем кнопки
    bot.send_message(message.chat.id, 'Выберите категорию анектодов : ', reply_markup=markup)  # созданные кнопки появятся после первого введенного текста

@bot.message_handler(content_types=["text"])
def Jokes(message):
    try:
        if message.text == "Короткие":
            bot.send_message(message.chat.id, listing_1[0])     # выводит первый анекдот из списка по данной категории анекдотов
            del listing_1[0]    # затем удаляет анекдот который был выведен позьзователю, чтобы анекдоты не повторялись

        if message.text == "Про программистов":
            bot.send_message(message.chat.id, listing_2[0])
            del listing_2[0]

        if message.text == "Для взрослых":
            bot.send_message(message.chat.id, listing_3[0])
            del listing_3[0]

        if message.text == "Для детей":
            bot.send_message(message.chat.id, listing_4[0])
            del listing_4[0]

        if message.text == "Чёрный юмор":
            bot.send_message(message.chat.id, listing_5[0])
            del listing_5[0]

        if message.text == "Про наркоманов":
            bot.send_message(message.chat.id, listing_6[0])
            del listing_6[0]

    except IndexError:            # обрабатывает ошибку IndexError, в случае если анекдоты в списке закончатся
        bot.send_message(message.chat.id,"Анекдоты этой категории закончались\n"
                                         "Выбери другую категорию анекдотов 😢")

bot.polling(none_stop=True, interval=0)      # Запускаем бота


