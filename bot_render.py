#!/usr/bin/env python3
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuração de logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o comando /start"""
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Olá {user.first_name}!\n"
        "✅ Bot funcionando perfeitamente no Render!"
    )

# Configuração da aplicação
app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    # Modo desenvolvimento (polling)
    app.run_polling()
