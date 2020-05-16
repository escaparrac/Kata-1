from telegram.ext import Updater


def main():
    updater = Update(token=open("./bot_token").read(), use_context=True)
    updater.start_polling()
    updater.idle()


main()