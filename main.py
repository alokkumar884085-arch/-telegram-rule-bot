import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("7730045851:AAH5RgKnC_i1uhJozqrzyEB0bsJVmHs-l5w")

WELCOME = """
🎉 Welcome to the Group!

Please read the rules:

1. Respect everyone.
2. No spam.
3. No scams.
4. No NSFW content.
5. No harassment.
6. Stay on topic.
7. Follow admin instructions.
8. Have fun!

Enjoy your stay! ❤️
"""

RULES = """
📜 GROUP RULES

1. Respect all members.
2. No abusive behavior.
3. No spam or flooding.
4. No advertisements.
5. No scams.
6. No NSFW content.
7. No hate speech.
8. No doxxing.
9. No impersonation.
10. Follow admin decisions.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👑 Owner Contact", url="https://t.me/Escrow2929")]
    ]
    await update.message.reply_text(
        WELCOME,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(RULES)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        keyboard = [
            [InlineKeyboardButton("👑 Owner Contact", url="https://t.me/Escrow2929")]
        ]
        await update.message.reply_text(
            f"🎉 Welcome {user.first_name}!\n\n{WELCOME}",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("rules", rules))
app.add_handler(
    MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
)

app.run_polling()
