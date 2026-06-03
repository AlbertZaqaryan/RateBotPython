from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from parser import parse_rate
from dotenv import load_dotenv
import os

load_dotenv()

bot = TeleBot(token=os.getenv('TOKEN'))



@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    btn_eur = KeyboardButton('EUR')
    btn_rub = KeyboardButton('RUB')
    btn_usd = KeyboardButton('USD')

    markup.add(btn_eur, btn_rub, btn_usd)

    bot.send_photo(message.chat.id, open('telebot.png', 'rb'))
    bot.send_message(
        message.chat.id,
        'Բարի գալուստ',
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text in ['EUR', 'RUB', 'USD'])
def currency_handler(message):
    rate_list = parse_rate()
    if message.text == 'EUR':
        bot.send_message(
            message.chat.id,
            f'Դուք ընտրեցիք {message.text}\nԿուրսը {rate_list[1]}'
        )
    elif message.text == 'USD':
        bot.send_message(
            message.chat.id,
            f'Դուք ընտրեցիք {message.text}\nԿուրսը {rate_list[0]}'
        )
    else:
        bot.send_message(
            message.chat.id,
            f'Դուք ընտրեցիք {message.text}\nԿուրսը {rate_list[2]}'
        )


bot.polling()