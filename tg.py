# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from datetime import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
reply_keyboard = [['/address', '/phone'],
                  ['/site', '/time']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
logger = logging.getLogger(__name__)


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
        reply_markup=markup
    )


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


# async def help_command(update, context):
# await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


async def address(update, context):
    await update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16")


async def phone(update, context):
    await update.message.reply_text("...")


async def site(update, context):
    await update.message.reply_text(
        "..")


async def work_time(update, context):
    await update.message.reply_text(
        "...")


async def time(update, context):
    await update.message.reply_text(
        f'Время: {datetime.now().time()}')


def main():
    application = Application.builder().token('5766938738:AAESBo31-dFz0P9j1j0gjz8zSN2JlgZvDbU').build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    application.add_handler(text_handler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("address", address))
    application.add_handler(CommandHandler("phone", phone))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("work_time", work_time))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.add_handler(CommandHandler("time", time))
    application.run_polling()


if __name__ == '__main__':
    main()
