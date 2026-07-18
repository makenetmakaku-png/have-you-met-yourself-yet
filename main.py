from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8868180441:AAGQlOI_iX9pmlmhdEaOFHNNeIjW8ZfPC94"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 It works!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling()