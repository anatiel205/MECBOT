#!/usr/bin/env python3
import os
#!/usr/bin/env python3
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Bot em modo produção!")

# Configuração profissional
app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv('PORT', 10000)),
        webhook_url=f"{os.getenv('WEBHOOK_URL')}/webhook",
        secret_token=os.getenv('WEBHOOK_SECRET'),
        drop_pending_updates=True
    )
