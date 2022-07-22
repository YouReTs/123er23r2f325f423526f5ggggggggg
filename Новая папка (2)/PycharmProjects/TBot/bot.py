import telebot
import config
import pb
import datetime
import pytz
import json
import traceback

P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Ну привет!\n" +
        "\n"
        "Чат💬           /chat\n"
        "\n"
        "[Cheker]🔍     /command1\n"
        "\n"
        "[Leaks]🗄      /command2\n"
        "[Dump's]🗂     /command3\n"
        "\n"
        "[Email] 📩     /acc_mail\n"
        "[Phone's]      /acc_phone\n"
        "[Login_Pass]   /acc_login\n"
        "[Pass]🔐       /pass\n"
        "[Hash]🔏       /hash\n"
        "\n"
        "[Dork's]⚠️  /dork\n"
        "\n"
        "Информация по курсу валют /exchange 📑.\n" +
        "Чтобы получить помощь        /help 🆘."
    )


@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('USD', callback_data='get-USD')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'),
        telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR')
    )

    bot.send_message(
        message.chat.id,
        'Click on the currency of choice:',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Обратная связь 📝', url='telegram.me/vferewvwrww'))
    bot.send_message(
        message.chat.id,
        "0) 0.Чат💬           /chat\n" +
        "\n" +
        "1) 1.[Cheker]🔍     /command1\n" +
        "\n" +
        "2) 2.[Leaks]🗄      /command2\n" +
        "3) 3.[Dump's]🗂     /command3\n" +
        "\n" +
        "4) 4.[Email] 📩     /acc_mail\n" +
        "5) 5.[Phone's]      /acc_phone\n" +
        "6) 6.[Login_Pass]   /acc_login\n" +
        "7) 7.[Pass]🔐       /pass\n" +
        "8) 8.[Hash]🔏       /hash\n" +
        "\n" +
        "9) 9.[Dork's]⚠️  /dork\n" +
        "\n" +
        "10) Информация по курсу валют /exchange 📑.\n" +
        "11) Чтобы получить помощь        /help 🆘.",
        reply_markup=keyboard
    )


@bot.message_handler(commands=['start_eco'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'ЭХО на связи. Напиши мне что-нибудь )')


# # Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# # Запускаем бота
@bot.message_handler(commands=['stop_eco'])
def stop(m, res=True):
    bot.send_message(m.chat.id, 'ЭХО стоп )')
    bot.polling(none_stop=False, interval=0)


# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)


# Шаг №7: обработчик для кнопок встроенной клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-'):
        get_ex_callback(query)


def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])


def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    ex = pb.get_exchange(ex_code)
    bot.send_message(
        message.chat.id, serialize_ex(ex),
        reply_markup=get_update_keyboard(ex),
        parse_mode='HTML'
    )


def get_update_keyboard(ex):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Update',
            callback_data=json.dumps({
                't': 'u',
                'e': {
                    'b': ex['buy'],
                    's': ex['sale'],
                    'c': ex['ccy']
                }
            }).replace(' ', '')
        ),
        telebot.types.InlineKeyboardButton('Share', switch_inline_query=ex['ccy'])
    )
    return keyboard


def serialize_ex(ex_json, diff=None):
    result = '<b>' + ex_json['base_ccy'] + ' -> ' + ex_json['ccy'] + ':</b>\n\n' + \
             'Buy: ' + ex_json['buy']
    if diff:
        result += ' ' + serialize_exchange_diff(diff['buy_diff']) + '\n' + \
                  'Sell: ' + ex_json['sale'] + \
                  ' ' + serialize_exchange_diff(diff['sale_diff']) + '\n'
    else:
        result += '\nSell: ' + ex_json['sale'] + '\n'
    return result


def serialize_exchange_diff(diff):
    print("123")
    # result = ''
    # if diff > 0:
    #    result = '(' + str(
    #        diff)# + ' <img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="↗️" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/72x72/2197.png">" src="https://s.w.org/images/core/emoji/72x72/2197.png">)'
    # elif diff < 0:
    #    result = '(' + str(diff)[
    #                   1:]# + ' <img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="↘️" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/72x72/2198.png">" src="https://s.w.org/images/core/emoji/72x72/2198.png">)'
    # return result


# Шаг №8: обработчик кнопки обновления
@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-'):
        get_ex_callback(query)
    else:
        try:
            if json.loads(data)['t'] == 'u':
                edit_message_callback(query)
        except ValueError:
            pass


def edit_message_callback(query):
    data = json.loads(query.data)['e']
    exchange_now = pb.get_exchange(data['c'])
    text = serialize_ex(
        exchange_now,
        get_exchange_diff(
            get_ex_from_iq_data(data),
            exchange_now
        )
    ) + '\n' + get_edited_signature()
    if query.message:
        bot.edit_message_text(
            text,
            query.message.chat.id,
            query.message.message_id,
            reply_markup=get_update_keyboard(exchange_now),
            parse_mode='HTML'
        )
    elif query.inline_message_id:
        bot.edit_message_text(
            text,
            inline_message_id=query.inline_message_id,
            reply_markup=get_update_keyboard(exchange_now),
            parse_mode='HTML'
        )


def get_ex_from_iq_data(exc_json):
    return {
        'buy': exc_json['b'],
        'sale': exc_json['s']
    }


def get_exchange_diff(last, now):
    return {
        'sale_diff': float("%.6f" % (float(now['sale']) - float(last['sale']))),
        'buy_diff': float("%.6f" % (float(now['buy']) - float(last['buy'])))
    }


def get_edited_signature():
    return '<i>Updated ' + \
           str(datetime.datetime.now(P_TIMEZONE).strftime('%H:%M:%S')) + \
           ' (' + TIMEZONE_COMMON_NAME + ')</i>'


# Шаг №9: встроенный режим
@bot.inline_handler(func=lambda query: True)
def query_text(inline_query):
    bot.answer_inline_query(
        inline_query.id,
        get_iq_articles(pb.get_exchanges(inline_query.query))
    )


def get_iq_articles(exchanges):
    result = []
    for exc in exchanges:
        result.append(
            telebot.types.InlineQueryResultArticle(
                id=exc['ccy'],
                title=exc['ccy'],
                input_message_content=telebot.types.InputTextMessageContent(
                    serialize_ex(exc),
                    parse_mode='HTML'
                ),
                reply_markup=get_update_keyboard(exc),
                description='Convert ' + exc['base_ccy'] + ' -> ' + exc['ccy'],
                thumb_height=1
            )
        )
    return result


bot.polling(none_stop=True)
