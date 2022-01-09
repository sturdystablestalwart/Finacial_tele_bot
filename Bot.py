import telebot

import config
import logick_01

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, config.opening_sticker_id)

    # keyboard
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("💵 Costs")
    item2 = telebot.types.KeyboardButton("📋 Yields")
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
            with open(logick_01.csv_yields(), "rb") as file:
                bot.send_document(message.chat.id, file)
            bot.send_message(message.chat.id, 'Вот пожалуйста!')
        else:
            bot.send_message(message.chat.id, 'Is it сложно to просто use buttons которые тебе дали?')


@bot.message_handler(content_types=['document'])
def handle_docs(message):
    bot.send_message(message.chat.id, 'Файл? Сейчас поглядим!')
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'received - ' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Скачал!')
    except Exception as e:
        bot.reply_to(message, str(e))



@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.send_message(message.chat.id, 'Я не умею слушать голосовые... пока что')


# RUN
bot.infinity_polling()
