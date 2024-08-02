import telebot
from commands import registerCommands
import json

with open('config.json', 'r') as file:
    config = json.load(file)

bot = telebot.TeleBot(token=config['token'], parse_mode='HTML')

registerCommands(bot)

def startup_print():
    print(f"📡 Conectado em: {bot.user.username} (@{bot.user.id}).")

startup_print(), bot.infinity_polling()
