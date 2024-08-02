from telebot import TeleBot
from telebot import types
import sqlite3
import json

with open('config.json', 'r') as file:
    config = json.load(file)

buttonProofs2 = types.InlineKeyboardButton('📦 Preview', url='https://saint2.su/embed/bPQKpwanrS8')
stripeLink = config['stripe_link']

keyboardProofs = types.InlineKeyboardMarkup()
keyboardProofs.add(buttonProofs2)


def startCommand(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def handler_start(message):
        bot.send_message(chat_id=message.from_user.id ,text=f'Hey, {message.from_user.first_name}. Follow our stripe link to continue with the purchase of the lifetime group of omegle videos.\n\n<b>Stripe:</b>\n{stripeLink}\n\nSend your proof of payment in this chat to proceed with the purchase.', reply_markup=keyboardProofs)

        banco = sqlite3.connect('data.db')
        cursor = banco.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS persons (id INTEGER)''')

        cursor.execute(f"SELECT 1 FROM persons WHERE id = {message.from_user.id}")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f"INSERT INTO persons (id) VALUES ({message.from_user.id})")
            banco.commit()

        banco.close()