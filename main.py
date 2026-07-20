from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8868180441:AAGQlOI_iX9pmlmhdEaOFHNNeIjW8ZfPC94"

WELCOME_MESSAGE = """
🌿 *Have You Met Yourself Yet?*

Welcome to the 200 Things To Do Alone Challenge.

For the next 200 days you'll complete one challenge each day, reflect on it, and earn points.

Today's Challenge:

☕ Drink your coffee without doing anything else at the same time.

Commands:
/journal - Submit today's journal
/help - Show commands
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    await update.message.reply_text(
        f"Hi {user}! 👋\n\n{WELCOME_MESSAGE}",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the challenge\n"
        "/journal - Submit today's journal\n"
        "/help - Show this menu"
    )

async def journal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Journal submissions aren't ready yet.\n\nThey'll be added next."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("journal", journal))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()