import telebot
from commands import registerCommands

bot = telebot.TeleBot(token='', parse_mode='HTML')

registerCommands(bot)

def startup_print():
    print(f"📡 Conectado em: {bot.user.username} (@{bot.user.id}).")

startup_print(), bot.infinity_polling()
