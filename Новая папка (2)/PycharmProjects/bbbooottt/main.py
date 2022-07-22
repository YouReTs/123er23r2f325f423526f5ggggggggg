# Auto-Bot
# Периодически в автоматическом режиме постит информацию в канал

import telebot  # pip install pyTelegramBotAPI
import requests
import time, datetime

# Токен, который выдает @botfather
bot = telebot.TeleBot('5416667430:AAGiAixxU1UTyKFJNiDQhYrD0IWp2WyONuw')

# Адрес телеграм-канала, начинается с @
# CHANNEL_NAME = '@et0test_bot'





eth_price = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR,RUB'
# print('1', ETH_price)

today = datetime.datetime.today()
# now = datetime.datetime.now()


def get_latest_eth_price():
    response = requests.get(eth_price)
    now1 = datetime.datetime.now
    response_json = response.json()
    return '<br>', ' DATE: ' + str(now1)[:19] + '   PRICE: ', response.json()  # 'PRICE'+.join(response_json)


print (get_latest_eth_price())


def format_eth_history(eth_history):
    rows = []
    for eth_price in eth_history:
        date = eth_price  # Форматирует дату в строку: '24.02.2018 15:09'
        price = eth_price

        # тег <b> делает текст полужирным
        row = date, price  # 24.02.2018 15:09: $<b>10123.4</b>
        rows.append(row)
    # Используйте тег <br> для создания новой строки
    return rows#'<br>'.join(rows)  # Join the rows delimited by <br> tag: row1<br>row2<br>row3


print('4')


def main():
    eth_history = []
    while True:
        price = get_latest_eth_price()
        date = datetime.datetime.now()
        eth_history.append({'date': date, 'price': price})

        # Отправка уведомления в Telegram   # Send a Telegram notification
        #bot.send_message(eth_history)
        if len(eth_history) == 5:  # После получения 5 объектов в ETC_history – отправляем обновление
            print('1', format_eth_history(eth_history))
            eth_history = []  # Reset the history   # Сброс истории
        time.sleep(3)  # Сон на 5 минут (Для тестовых целей вы можете указать меньшее число)


# Пока не закончатся шутки, посылаем их в канал
#for price in ():
#    bot.send_message(CHANNEL_NAME, "123")
# Делаем паузу в один час
#    time.sleep(3600)
#bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')



# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


if __name__ == '__main__':
    main()
