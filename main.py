from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)

from database import conn, cursor

TOKEN = "8868180441:AAGQlOI_iX9pmlmhdEaOFHNNeIjW8ZfPC94"

ASK_NAME = 1

# ---------------- REGISTER ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    cursor.execute(
        "SELECT * FROM users WHERE id=?",
        (user.id,)
    )

    exists = cursor.fetchone()

    if exists:
        await update.message.reply_text(
            f"🌿 Welcome back, {exists[1]}!\n\nUse /profile to see your progress."
        )
        return ConversationHandler.END

    await update.message.reply_text(

"""🌿 Have You Met Yourself Yet?

Welcome to the 200 Things To Do Alone Challenge.

Before we begin...

What's your name?"""
    )

    return ASK_NAME


async def save_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    name = update.message.text

    cursor.execute(
        "INSERT INTO users(id,name) VALUES(?,?)",
        (
            update.effective_user.id,
            name,
        ),
    )

    conn.commit()

    await update.message.reply_text(

f"""Welcome, {name}! 🌱

You are officially registered.

Today's Challenge:

☕ Drink your coffee without doing anything else at the same time.

When you're done use

/journal

Good luck!"""
    )

    return ConversationHandler.END


# ---------------- PROFILE ----------------

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    cursor.execute(
        "SELECT name,points,streak FROM users WHERE id=?",
        (update.effective_user.id,),
    )

    row = cursor.fetchone()

    if not row:
        await update.message.reply_text(
            "Register first with /start"
        )
        return

    await update.message.reply_text(

f"""👤 {row[0]}

⭐ Points: {row[1]}
🔥