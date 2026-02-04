import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "TOKEN_SE_DE_O_RAILWAY"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    names = re.findall(r"Tên tài khoản:\s*(.+)", text)
    accounts = re.findall(r"Số tài khoản:\s*(\d+)", text)

    if not names or not accounts:
        await update.message.reply_text("❌ Không tìm thấy dữ liệu hợp lệ")
        return

    result = "\n".join(f"{n} | {a}" for n, a in zip(names, accounts))
    await update.message.reply_text(result)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()
