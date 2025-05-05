import telebot
import requests
import pytesseract
from PIL import Image
import os

# Dados reais de produção
TOKEN = "7885605169:AAH8nbOHHjYZu4EcYYVHD0zSCJzMBT3mwho"
URL_CONSULTA = "https://mecbot-s5l5.onrender.com"

bot = telebot.TeleBot(TOKEN)

def consultar_placa(placa):
    try:
        resposta = requests.get(f"{URL_CONSULTA}/placa/{placa}")
        if resposta.status_code == 200:
            return resposta.text
        return "Erro ao consultar a placa."
    except Exception as e:
        return f"Erro: {e}"

@bot.message_handler(content_types=['text'])
def receber_texto(mensagem):
    placa = mensagem.text.strip().upper()
    if len(placa) >= 7:
        resposta = consultar_placa(placa)
        bot.reply_to(mensagem, resposta)
    else:
        bot.reply_to(mensagem, "Por favor, envie uma placa válida.")

@bot.message_handler(content_types=['photo'])
def receber_foto(mensagem):
    try:
        file_id = mensagem.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)

        with open("placa.jpg", "wb") as f:
            f.write(file)

        imagem = Image.open("placa.jpg")
        texto = pytesseract.image_to_string(imagem).upper()
        placa = ''.join(filter(str.isalnum, texto))[:7]
        resposta = consultar_placa(placa)
        bot.reply_to(mensagem, f"Placa detectada: {placa}\n{resposta}")
    except Exception as e:
        bot.reply_to(mensagem, f"Erro ao processar a imagem: {e}")

def iniciar_bot():
    bot.polling()
