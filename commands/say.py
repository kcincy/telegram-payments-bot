from telebot import TeleBot

def saySomething(bot: TeleBot):
    @bot.message_handler(commands=['say'])
    def handle_printar(message):
        try:
            parametros = message.text[len('/say '):].strip().split(' ', 1)
        
            chat_id, mensagem = parametros
            
            bot.send_message(chat_id=chat_id, text=mensagem)
            
            bot.reply_to(message, "✅ <b>Mensagem enviada com sucesso.</b>")
        except Exception as e:
            bot.reply_to(message, f'❌ <b>Ocorreu um erro: {e}</b>')