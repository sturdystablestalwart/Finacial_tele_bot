import telebot
import config
import logick_01
from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, config.opening_sticker_id)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("💵 Costs")
    item2 = types.KeyboardButton("📋 Yields")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nI am - <b>{1.first_name}</b>, бот created to отправлять you "
                     "инвестиционные данные.".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def refreshed_parse(message):
    if message.chat.type == 'private':
        if message.text == '💵 Costs':
            bot.send_message(message.chat.id, 'Секунду, сейчас пришлю!')
            with open(logick_01.csv_costs(), "rb") as file:
                bot.send_document(message.chat.id, file)
            bot.send_message(message.chat.id, 'Вот пожалуйста!')
        elif message.text == '📋 Yields':
            bot.send_message(message.chat.id, 'Момент, сейчас пришлю!')
            with open(logick_01.csv_yeilds(), "rb") as file:
                bot.send_document(message.chat.id, file)
            bot.send_message(message.chat.id, 'Вот пожалуйста!')
        else:
            bot.send_message(message.chat.id, 'Is it сложно to просто use buttons которые тебе дали?')


# RUN
bot.infinity_polling()
