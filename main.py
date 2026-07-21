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

1. Respect everyone.
2. No spam.
3. No scams.
4. No NSFW content.
5. No harassment.
6. Stay on topic.
7. Follow admin instructions.

━━━━━━━━━━━━━━━━━━

🤖 Bot Status: {BOT_STATUS}

{status_text}

━━━━━━━━━━━━━━━━━━

Thank you for following the rules.
"""

{status_text}

text = f"""
📜 GROUP RULES

━━━━━━━━━━━━━━━━━━

🤖 Bot Status: {BOT_STATUS}

{status_text}

━━━━━━━━━━━━━━━━━━
"""

Need help? Contact the owner below.
"""

    await update.message.reply_text(
        text,
        reply_markup=keyboard,
    )
