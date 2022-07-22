# Auto-Bot
# Периодически в автоматическом режиме постит информацию в канал

import telebot  # pip install pyTelegramBotAPI
import requests
import time
from datetime import datetime
import telebot  # pip install
from telebot import apihelper

# Использование прокси в telebot
# apihelper.proxy = {'https':'socks5://login:password@ip:port'}


# Токен, который выдает @botfather
token = '5416667430:AAGiAixxU1UTyKFJNiDQhYrD0IWp2WyONuw'
bot = telebot.TeleBot(token)
chat_id = '5195681649'


requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), params=dict(
   chat_id='5195681649',
   text='Hello world!'))


# Обработчик start
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока',)
    keyboard.row('/test', '/test', '/test')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)


# InLine клавиатура
@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()  # markup объявляет новую переменную с inline keyboard, а
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))  # markup.add – создает отдельную кнопку
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))  # text - отвечает за текст на кнопке
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))  # callback_data - данные от юзера
    bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':if not os.path.isdir("SORT"):
        bot.send_message(message.chat.id, 'Ещё раз привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    # bot.answer_callback_quer – это всплывающее окно, которое будет показано пользователю после нажатия кнопки.
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == '3':  # call.data - значение которое указывали при создании клавиатуры в параметре callback_data.
        answer = 'Вы троечник!'
    elif call.data == '4':
        answer = 'Вы хорошист!'
    elif call.data == '5':
        answer = 'Вы отличник!'

    bot.send_message(call.message.chat.id, answer)
    #  клавиатура будет исчезать из чата. Это можно сделать добавив в конец функции query_handler следующую строку:
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id) # Это функция редактирования клавиатуры
    # , вызванная без указания объекта клавиатуры. Теперь после ответа пользователя клавиатура будет убрана ботом:





BITCOIN_API_URL = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR,RUB'

#coin = ETH
#coin2 = BTC,USD,EUR,RUB

#BITCOIN_API_URL = 'https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms={coin2}'
#BITCOIN_API_URL = 'https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms={coin2}'.format(coin())
#coin = 'ETH'

print(BITCOIN_API_URL)


def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    date1 = datetime.now()
    response_json1 = str(date1)[:19] + '\n' + str(response_json)
    return response_json1


def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date1 = datetime.now
        #date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')  # Форматирует дату в строку: '24.02.2018 15:09'
        #print(date)
        price = get_latest_bitcoin_price
        #price = bitcoin_price['price']
        # тег <b> делает текст полужирным
        #row = '{}: $<b>{}</b>'.format(date, price)  # 24.02.2018 15:09: $<b>10123.4</b>
        row = (date1, price)  # 24.02.2018 15:09: $<b>10123.4</b>
        rows.append(row)
        #print(rows)
    #print('<br>'.join(rows))
    #return '<br>'.join(rows)  # Используйте тег <br> для создания новой строки
    return rows  # Используйте тег <br> для создания новой строки


def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        print('Получение цены:', price)
        date2 = datetime.now()
        bitcoin_history.append({'Date': date2, 'Price': price})
        print(bitcoin_history)
       # Отправка уведомления в Telegram
        if len(bitcoin_history) == 3:  # После получения 5 объектов в bitcoin_history – отправляем обновление
            #post = ('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            post = (format_bitcoin_history(bitcoin_history))
            print(post)
            #post_ifttt_webhook('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), params=dict(
                chat_id='5195681649',
                text=get_latest_bitcoin_price()))
            bitcoin_history = []  # Сброс истории
        time.sleep(1 * 10)  # Сон на 5 минут(Для тестовых целей вы можете указать меньшее число)



if __name__ == '__main__':
    main()

bot.polling(none_stop=True, timeout=30)
