#!/usr/bin/env python3
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuração de logs detalhada
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
        f"🚀 Bot operacional! Olá {user.first_name}!\n"
        "🔗 Hosteado no Render.com"
    )

def main():
    try:
        app = Application.builder().token(TELEGRAM_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        if os.getenv('RENDER'):
            logger.info("Iniciando em modo Webhook")
            app.run_webhook(
                listen="0.0.0.0",
                port=int(os.getenv('PORT', 10000)),
                webhook_url=f"{os.getenv('WEBHOOK_URL')}/webhook",
                secret_token=os.getenv('WEBHOOK_SECRET'),
                drop_pending_updates=True
            )
        else:
            logger.info("Iniciando em modo Polling")
            app.run_polling()
            
    except Exception as e:
        logger.error(f"Falha crítica: {str(e)}")
        raise

if __name__ == "__main__":
    main()
