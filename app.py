import os
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters	
from conf.settings import bot_token,bot_user_name, URL
from flask import Flask
from comandos import comandos
global TOKEN


TOKEN = bot_token

updater = Updater(token= TOKEN,use_context=True)
dispatcher = updater.dispatcher

app = Flask(__name__)

@app.route('/{}'.format(TOKEN),methods=['POST'])
def welcome(update, context):
	for member in update.message.new_chat_members:
		update.message.reply_text("{username} Welcome to the party!!\U0001F47E\nse apresente por favor e não esqueça de entrar no grupo de avisos:t.me/avisosEDS".format(username=member.username))
	return 'ok'


@app.route('/setwebhook',methods=['GET','POST'])
def set_webhook():
	s = updater.bot.setWebhook('{URL}{HOOK}'.format(URL=URL,HOOK=TOKEN))

	if s:
		return "webhook setup ok"
	else:
		return "webhook setup failed"



welcome_handler = MessageHandler(Filters.status_update.new_chat_members,welcome)
dispatcher.add_handler(welcome_handler)

updater.start_polling()


@app.route('/')
def index():
	return 'index'

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0',port=port)