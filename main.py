import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_STATUS = "🟢 Online"

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👑 Owner Contact", url="https://t.me/Escrow2929")]
    ])

    status_text = (
        "✅ Bot is working perfectly."
        if BOT_STATUS == "🟢 Online"
        else "🟠 Bot is currently under maintenance."
    )

    text = f"""
📜 GROUP RULES

1️⃣ Respect everyone.
2️⃣ No spam or flooding.
3️⃣ No advertising.
4️⃣ No scams or fake giveaways.
5️⃣ No NSFW content.
6️⃣ No harassment or bullying.
7️⃣ Stay on topic.
8️⃣ Respect admins.
9️⃣ No hate speech.
🔟 Follow Telegram Terms of Service.

━━━━━━━━━━━━━━━━━━

🤖 Bot Status: {BOT_STATUS}

{status_text}

━━━━━━━━━━━━━━━━━━

Need help?
Contact the owner using the button below.

❤️ Thank you for following the rules!
"""

    await update.message.reply_text(
        text,
        reply_markup=keyboard,
    )

def main():
    token = "7730045851:AAH5RgKnC_i1uhJozqrzyEB0bsJVmHs-l5w"
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("rules", rules))

    print("Bot is polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
