from typing import BinaryIO

import telebot
from telebot import types

token = '5378947119:AAF34TLlTDwK4DFHyfjVlDRT_j3d34SIxNQ'

bot = telebot.TeleBot(token)
bulochka_in = True
cutie_in = True
bulochka = '\U0001f408\u200D\u2B1BBulochka'
bulochka_outside = open('bul_out.mp4', 'rb')
cutie_outside = open('cutie_out.mp4', 'rb')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Check status')
    item2 = types.KeyboardButton('Update status')
    item3 = types.KeyboardButton('See pictures')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Hi,{0.first_name}'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text', 'video', 'images'])
def bot_message(message):
    global bulochka_in, cutie_in, bulochka, bulochka_outside, cutie_outside
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Check status')
    item1a = types.KeyboardButton('Check status again')
    item2 = types.KeyboardButton('Update status')
    item3 = types.KeyboardButton('See pictures')
    bul_out = types.KeyboardButton('\U0001f408\u200D\u2B1BBulochka is outside')
    bul_in = types.KeyboardButton('\U0001f408\u200D\u2B1B\U0001f3e0Bulochka is inside')
    cut_out = types.KeyboardButton('\U0001F431Cutie is outside')
    cut_in = types.KeyboardButton('\U0001F431\U0001f3e0Cutie is inside')
    back = types.KeyboardButton('Back')
    if message.chat.type == 'private':
        if message.text == 'Check status' or message.text == 'Check status again':
            if bulochka_in == True and bulochka_in == cutie_in:
                bot.send_message(message.chat.id, f'\U0001F431Cutie and {bulochka} are at home', reply_markup=markup)
                markup.add(item1a, item2, back)
                bot.send_sticker(message.chat.id, open('home_state.webp', 'rb'))
            elif bulochka_in == False and bulochka_in == cutie_in:
                markup.add(item1a, item2, back)
                bot.send_message(message.chat.id, f'\U0001F431Cutie and {bulochka} are playing outside',
                                 reply_markup=markup)
                bot.send_sticker(message.chat.id, open('both_outside.webp', 'rb'))
            elif bulochka_in == True and bulochka_in != cutie_in:
                markup.add(item1a, item2, back)
                bot.send_message(message.chat.id,
                                 f'\U0001F431Cutie is playing outside and \U0001f3e0{bulochka} is inside',
                                 reply_markup=markup)
            else:
                markup.add(item1a, item2, back)
                bot.send_message(message.chat.id, 'Bulochka is playing outside and \U0001f3e0\U0001F431Cutie is '
                                                  'sleeping inside', reply_markup=markup)
        elif message.text == 'Update status':
            markup.add(bul_in, bul_out, cut_in, cut_out, back)
            bot.send_message(message.chat.id, 'Who\'s status do you want to update?', reply_markup=markup)
        elif message.text == '\U0001f408\u200D\u2B1BBulochka is outside':
            markup.add(item1, back)
            bulochka_in = False
            bot.send_message(message.chat.id, 'Bulochka\'s status was updated, Enjoy your walking, Bulochka!',
                             reply_markup=markup)
            bot.send_video(message.chat.id, bulochka_outside)
        elif message.text == '\U0001f408\u200D\u2B1B\U0001f3e0Bulochka is inside':
            markup.add(item1, back)
            bulochka_in = True
            bot.send_message(message.chat.id, 'Bulochka status was updated, Sweet dreams, Bulochka!',
                             reply_markup=markup)
        elif message.text == '\U0001F431Cutie is outside':
            markup.add(item1, back)
            cutie_in = False
            bot.send_message(message.chat.id, '\U0001F431 Cutie\'s status was updated, Enjoy your walking, Cutie!',
                             reply_markup=markup)
            bot.send_video(message.chat.id, cutie_outside)
        elif message.text == '\U0001F431\U0001f3e0Cutie is inside':
            markup.add(item1, back)
            cutie_in = True
            bot.send_message(message.chat.id, 'Cutie\'s status was updated, Sweet dreams, Cutie!',
                             reply_markup=markup)
        elif message.text == 'Back':
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Let\'s start again. How can I help you?',
                             reply_markup=markup)
        else:
            markup.add(back)
            bot.send_message(message.chat.id, 'Sorry, I didn\'t get it, let\'s try again :) ', reply_markup=markup)


bot.polling(none_stop=True)
