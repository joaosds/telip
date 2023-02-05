from config import TOKEN, CHAT_ID_LIST
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    if user_id not in CHAT_ID_LIST:
        print(f"User of id {user_id} tried starting the bot.")
        await context.bot.send_message(
            chat_id=user_id,
            text="010010110101010101010110101000101010111010101011011101010110",
        )

    else:
        res = requests.get("https://ifconfig.me")
        await context.bot.send_message(chat_id=user_id, text=res.text)


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)
    application.run_polling()
