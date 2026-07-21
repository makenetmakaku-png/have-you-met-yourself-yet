from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from database import conn, cursor

TOKEN = "8868180441:AAGQlOI_iX9pmlmhdEaOFHNNeIjW8ZfPC94"

# ---------- START ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    cursor.execute(
        "SELECT * FROM users WHERE id=?",
        (user.id,)
    )

    row = cursor.fetchone()

    if row is None:

        cursor.execute(
            """
            INSERT INTO users
            (id,name,points,streak,current_day)
            VALUES(?,?,?,?,?)
            """,
            (
                user.id,
                user.first_name,
                0,
                0,
                1
            )
        )

        conn.commit()

        await update.message.reply_text(
f"""🌿 Have You Met Yourself Yet?

Welcome, {user.first_name}.

This isn't a productivity challenge.

It's 200 small invitations to slow down, notice, and reconnect with yourself.

You're officially registered.

Type

/today

to begin."""
        )

    else:

        await update.message.reply_text(
f"""🌿 Welcome back, {row[1]}.

Current Score ⭐ {row[2]}
Current Streak 🔥 {row[3]}

Use /today."""
        )

# __________ RESET __________
async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (update.effective_user.id,)
    )
    conn.commit()
    await update.message.reply_text("Your account has been reset.")
# ---------- TODAY ----------

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):

    cursor.execute(
        "SELECT current_day FROM users WHERE id=?",
        (update.effective_user.id,)
    )

    row = cursor.fetchone()

    if row is None:
        await update.message.reply_text(
            "Please register first using /start"
        )
        return

    day = row[0]

    cursor.execute(
        "SELECT text FROM challenges WHERE day=?",
        (day,)
    )

    challenge = cursor.fetchone()

    if challenge:

        await update.message.reply_text(
f"""🌿 Day {day}/200

Today's Invitation

{challenge[0]}

When you're done...

Type

/journal"""
        )

    else:

        await update.message.reply_text(
            "Challenge not found."
        )

# ---------- PROFILE ----------

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    cursor.execute(
        """
        SELECT
        name,
        points,
        streak,
        current_day
        FROM users
        WHERE id=?
        """,
        (update.effective_user.id,)
    )

    row = cursor.fetchone()

    if row:

        await update.message.reply_text(
f"""👤 {row[0]}

⭐ Score: {row[1]}

🔥 Streak: {row[2]}

📖 Page: {row[3]}/200"""
        )

# ---------- LEADERBOARD ----------

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    cursor.execute(
        """
        SELECT
        name,
        points
        FROM users
        ORDER BY points DESC
        """
    )

    users = cursor.fetchall()

    text = "🏆 Travelers\n\n"

    medal = ["🥇","🥈","🥉"]

    for i,user in enumerate(users):

        if i < 3:
            prefix = medal[i]
        else:
            prefix = f"{i+1}."

        text += f"{prefix} {user[0]} — ⭐ {user[1]}\n"

    await update.message.reply_text(text)

# ---------- JOURNAL ----------

async def journal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
"""📝

Journal saving is the next feature.

It will open a writing mode here."""
    )

# ---------- BOT ----------

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("today",today))
app.add_handler(CommandHandler("profile",profile))
app.add_handler(CommandHandler("leaderboard",leaderboard))
app.add_handler(CommandHandler("journal",journal))
app.add_handler(CommandHandler("reset", reset))

print("Bot Running...")

app.run_polling()