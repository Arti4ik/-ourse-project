import telebot
import requests
import random
from config import token
from telebot import types
from bs4 import BeautifulSoup as b


# Короткие анекдоты
URL_1 = "https://anekdoty.ru/korotkie/"
def parser_1(url):
    r = requests.get(url=url)
    soup_1 = b(r.text, "html.parser")
    anekdots_1 = soup_1.find_all("div", class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_1]
listing_1 = parser_1(URL_1)
random.shuffle(listing_1)

# Анекдоты про программистов
URL_2 = "https://anekdoty.ru/pro-programmistov/"
def parser_2(url):
    r = requests.get(url)
    soup_2 = b(r.text, "html.parser")
    anekdots_2 = soup_2.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_2]
listing_2 = parser_2(URL_2)
random.shuffle(listing_2)

# Анекдоты для взрослыхz
URL_3 = "https://anekdoty.ru/pro-vzroslyh/"
def parser_3(url):
    r = requests.get(url)
    soup_3 = b(r.text, "html.parser")
    anekdots_3 = soup_3.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_3]
listing_3 = parser_3(URL_3)
random.shuffle(listing_3)

# Анекдоты для детей
URL_4 = "https://anekdoty.ru/detskie/"
def parser_4(url):
    r = requests.get(url)
    soup_4 = b(r.text, "html.parser")
    anekdots_4 = soup_4.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_4]
listing_4 = parser_4(URL_4)
random.shuffle(listing_4)

# Анекдоты про чёрный юмор
URL_5 = "https://anekdoty.ru/detskie/"
def parser_5(url):
    r = requests.get(url)
    soup_5 = b(r.text, "html.parser")
    anekdots_5 = soup_5.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_5]
listing_5 = parser_5(URL_5)
random.shuffle(listing_5)

# Анекдоты про Наркоманов
URL_6 = "https://anekdoty.ru/pro-narkomanov/"
def parser_6(url):
    r = requests.get(url)
    soup_6 = b(r.text, "html.parser")
    anekdots_6 = soup_6.find_all("div",class_="holder")
    return [i.text.split('#')[-2] for i in anekdots_6]
listing_6 = parser_6(URL_6)
random.shuffle(listing_6)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
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
    markup.add(item1,item2,item3,item4,item5,item6)
    bot.send_message(message.chat.id, 'Выберите категорию анектодов : ', reply_markup=markup)

@bot.message_handler(commands=["holiday"])
def welcome(message):
    bot.send_message(message.chat.id, '')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите категорию поздравлений : ', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def Jokes(message):
    try:
        if message.text == "Короткие":
            bot.send_message(message.chat.id, listing_1[0])
            del listing_1[0]

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

    except IndexError:
        bot.send_message(message.chat.id,"Анекдоты этой категории закончались\n"
                                         "Выбери другую категорию анекдотов 😢")

bot.polling(none_stop=True, interval=0)


