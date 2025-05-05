#!/usr/bin/env python3
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuração básica
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"👋 Olá {user.first_name}! Bot conectado ao Render.")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    if os.getenv('RENDER'):
        app.run_webhook(
            listen="0.0.0.0",
            port=int(os.getenv('PORT', 10000)),
            webhook_url=f"{os.getenv('WEBHOOK_URL')}/webhook"
        )
    else:
        app.run_polling()

if __name__ == "__main__":
    main()
