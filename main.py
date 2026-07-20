from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from database import cursor

TOKEN = "8868180441:AAGQlOI_iX9pmlmhdEaOFHNNeIjW8ZfPC94"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    cursor.execute(
        "SELECT * FROM users WHERE id=?",
        (user.id,)
    )

    row = cursor.fetchone()

    if row:
        await update.message.reply_text(
            f"🌿 Welcome back, {row[1]}!"
        )
    else:
        cursor.execute(
            "INSERT INTO users(id,name) VALUES(?,?)",
            (user.id, user.first_name)
        )

        cursor.connection.commit()

        await update.message.reply_text(
            f"""🌿 Welcome, {user.first_name}!

You've been registered!

Today's challenge:

☕ Drink your coffee without doing anything else.

Commands:

/profile
/leaderboard
/journal"""
        )


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    cursor.execute(
        "SELECT name,points,streak FROM users WHERE id=?",
        (update.effective_user.id,)
    )

    row = cursor.fetchone()

    if row:
        await update.message.reply_text(
            f"""👤 {row[0]}

⭐ Points: {row[1]}
🔥 Streak: {row[2]}

Day 1 / 200"""
        )


async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    cursor.execute(
        "SELECT name,points FROM users ORDER BY points DESC"
    )

    rows = cursor.fetchall()

    text = "🏆 Leaderboard\n\n"

    for i, row in enumerate(rows, 1):
        text += f"{i}. {row[0]} — {row[1]}⭐\n"

    await update.message.reply_text(text)


async def journal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 Journal feature coming next."
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("profile", profile))
app.add_handler(CommandHandler("leaderboard", leaderboard))
app.add_handler(CommandHandler("journal", journal))

print("Bot running...")

app.run_polling()