from telegram.ext import Updater, CommandHandler


def main():
    # Instanciamos el updator
    updater = Updater(token=open("./bot_token").read(), use_context=True)

    # Añadiendo un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Empezamos a pedir notificaciones a Telegram
    updater.start_polling()
    
    # Capturamos señales de parada
    updater.idle()

    def start(update, context):
    pass


main()