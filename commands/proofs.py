from telebot import TeleBot
from telebot import types
import re
import json

with open('config.json', 'r') as file:
    config = json.load(file)

approvalGroup = config['chat_id']
groupLink = config['group_link']

allowAcess = types.InlineKeyboardButton('✅ Liberar Acesso', callback_data='allowAcessFunc')
confirm = types.InlineKeyboardButton('✅ Confirmar', callback_data='confirmFunc')
cancel = types.InlineKeyboardButton('❌ Cancelar', callback_data='cancelFunc')
delete = types.InlineKeyboardButton('🗑 Excluir', callback_data='deleteFunc')
deleteForced = types.InlineKeyboardButton('🗑 Excluir', callback_data='confirmFunc')

buttonPornContent = types.InlineKeyboardButton('🔧 Fix Group Ban', url='https://t.me/pornographiccontent')
keyboardPornContent = types.InlineKeyboardMarkup()
keyboardPornContent.add(buttonPornContent)

keyboard = types.InlineKeyboardMarkup()
keyboard.add(allowAcess, delete)

keyboardAllowed = types.InlineKeyboardMarkup()
keyboardAllowed.add(deleteForced)

confirmButtons = types.InlineKeyboardMarkup()
confirmButtons.add(confirm, cancel)
def saySomething(bot: TeleBot):
    @bot.message_handler(commands=['a'])
    def print_parameters(message):
        try:
            parameters = message.text.split('/a', 1)[1].strip().split()
            if len(parameters) != 2:
                bot.reply_to(message, text="🚨 <b>Você deve passar exatamente dois parâmetros.</b>")
                return
            param1, param2 = parameters
            bot.send_message(chat_id=f'{param1}', text=f'<b>Your access link:</b>\n\n{param2}')
            bot.reply_to(message, text='✅ <b>Link enviado com sucesso.</b>')
        except Exception:
            bot.reply_to(message, text='❌ <b>Ocorreu um erro ao enviar o link.</b>')

def approvalButtonFunc(bot: TeleBot):
        @bot.callback_query_handler(func=lambda call: call.data == 'allowAcessFunc')
        def callback_query(call):
                
            match = re.search(r'ID do Cliente: (\d+)', call.message.caption or call.message.text)
            cliente_id = match.group(1)

            try:
                bot.send_message(chat_id=f'{cliente_id}', text=f'<b>Your access link:</b>\n\n{groupLink}')
                bot.send_message(chat_id=f'{cliente_id}', text=f'If you see “This Group Has Been Banned For Spreading Pornographic Content” you can still join and view that content in a fast and secure way by following the instructions in this channel.', reply_markup=keyboardPornContent)
                bot.reply_to(call.message, text='✅ <b>Link sent successfully.</b>')
            except Exception as e:
                 bot.reply_to(call.message, f'❌ <b>Ocorreu um erro: {e}</b>')

            if call.message.photo == None:
                    bot.edit_message_text(text=call.message.text, chat_id=approvalGroup, message_id=call.message.message_id, reply_markup=keyboardAllowed)
            else:
                    bot.edit_message_caption(caption=call.message.caption, chat_id=approvalGroup, message_id=call.message.message_id, reply_markup=keyboardAllowed)

def deleteFunc(bot: TeleBot):
    @bot.callback_query_handler(func=lambda call: call.data == 'deleteFunc')
    def callback_query(call):

        if call.message.photo == None:
                bot.edit_message_text(text=call.message.text, chat_id=approvalGroup, message_id=call.message.message_id, reply_markup=confirmButtons)
        else:
                bot.edit_message_caption(caption=call.message.caption, chat_id=approvalGroup, message_id=call.message.message_id, reply_markup=confirmButtons)
        

def cancelFunc(bot: TeleBot):
    @bot.callback_query_handler(func=lambda call: call.data == 'cancelFunc')
    def callback_query(call):

        if call.message.photo == None:
                bot.edit_message_text(text=call.message.text, chat_id=approvalGroup, message_id=call.message.message_id, reply_markup=keyboard)
        else:
                bot.edit_message_caption(caption=call.message.caption, chat_id=approvalGroup, message_id=call.message.message_id, reply_markup=keyboard)

def confirmFunc(bot: TeleBot):
    @bot.callback_query_handler(func=lambda call: call.data == 'confirmFunc')
    def callback_query(call):
        bot.delete_message(approvalGroup, call.message.message_id)


def proofCollection(bot: TeleBot):
    @bot.message_handler(content_types=['photo'])
    def handler_photo(message):

            file_id = message.photo[-1].file_id

            bot.send_photo(chat_id=approvalGroup, photo=file_id, caption=f'👤 Cliente: {message.from_user.first_name} (@{message.from_user.username})\n🆔 ID do Cliente: {message.from_user.id}\n📌 Legenda: {message.caption}', reply_markup=keyboard)

            bot.reply_to(message, text='<b>Proof of payment sent successfully. Wait for your invitation link to be sent, this action may take a while, be patient.</b>')


    @bot.message_handler(content_types=['text'])
    def handler_document(message):
            
            if "t.me" in message.text:
                return
            else: bot.send_message(chat_id=approvalGroup, text=f'{message.text}\n\n👤 Cliente: {message.from_user.first_name} (@{message.from_user.username})\n🆔 ID do Cliente: {message.from_user.id}', reply_markup=keyboard)