import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ChatJoinRequestHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8614104917:AAGLfy0Xut-B-g6BW95C8-mv7eHFap3JEoA"
CHANNEL_ID = -1001971781694
IMAGE_URL = "https://i.ibb.co/Qj98sm31/photo-2026-05-15-22-03-17.jpg"

WELCOME_MESSAGE = (
    "Qoutex Compounding series group click this link 🔗 👇\n\n"
    "https://t.me/+38IXH_QUK6EyMWY1\n"
    "https://t.me/+38IXH_QUK6EyMWY1\n\n"
    "🔥 Just 2 Days Challenge! 🔥\n"
    "Turn $10 → $500 💸\n"
    "Limited slots — Join Fast & Start Earning Now! 🚀"
)

async def handle_join_request(update, context):
    user = update.chat_join_request.from_user
    chat_id = user.id
    keyboard = [[InlineKeyboardButton("✅ Join Group Now", url="https://t.me/+38IXH_QUK6EyMWY1")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMAGE_URL,
            caption=WELCOME_MESSAGE,
            reply_markup=reply_markup
        )
        logger.info(f"Welcome sent to {user.first_name}")
        # await update.chat_join_request.approve()
    except Exception as e:
        logger.error(f"Error: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    logger.info("Bot started 24/7!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
