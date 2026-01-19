import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask
from threading import Thread
import os

# --- CONFIGURAÇÃO DE CREDENCIAIS ---
# Seu Token
TOKEN = "8590639855:AAG4F62QVn2ljYiLaGA3G_vJtA4Fko7yHVk"

# ⚠️ IMPORTANTE: Cole aqui o link do seu site no GitHub Pages
# Exemplo: "https://seu-usuario.github.io/zeus-p2p"
APP_URL = "https://thxweb3dev.github.io/zeusp2pfinance" 

# Inicializa o Bot
bot = telebot.TeleBot(TOKEN)

# --- SERVIDOR WEB PARA MANTER O BOT ONLINE 24H ---
app = Flask('')

@app.route('/')
def home():
    return "ZEUS System Online! ⚡️"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- LÓGICA DO BOT (/START) ---
@bot.message_handler(commands=['start'])
def enviar_boas_vindas(message):
    # Coleta Nome e Username
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username
    
    # Formata a saudação: Nome | @Username (ou apenas Nome se não tiver user)
    if user_username:
        saudacao = f"Olá, <b>{user_first_name} | @{user_username}</b>!"
    else:
        saudacao = f"Olá, <b>{user_first_name}</b>!"

    # Texto atualizado conforme solicitado
    texto = (
        f"{saudacao}\n\n"
        "Seja bem-vindo ao <b>ZEUS⚡️P2P | Finance</b>.\n\n"
        "Somos o futuro das finanças descentralizadas.\n\n"
        "🔹 Realize Depósitos, Cobranças e Saques via PIX.\n"
        "🔹 Liquide Faturas e faça Saques via Cripto.\n"
        "🔹 Pague Boletos de até R$ 20.000,00.\n\n"
        "<b>Tudo isso sem burocracias e sem KYC.</b>\n\n"
        "👇 <b>Clique abaixo para acessar o App:</b>"
    )

    # Criação do botão que abre o Mini App
    markup = InlineKeyboardMarkup()
    botao_app = InlineKeyboardButton(text="📱 Acessar ZEUS App", web_app=WebAppInfo(url=APP_URL))
    markup.add(botao_app)

    # Envia a mensagem
    bot.send_message(message.chat.id, texto, parse_mode="HTML", reply_markup=markup)

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    keep_alive() # Inicia o servidor web
    
    # CORREÇÃO DO ERRO 409:
    print("♻️ Limpando conflitos de webhook...")
    bot.remove_webhook() # Remove qualquer conexão presa anterior
    
    import time
    time.sleep(1) # Espera 1 segundo para garantir
    
    print("🚀 Bot iniciado!")
    # skip_pending=True ignora mensagens velhas acumuladas para não travar na inicialização
    bot.infinity_polling(skip_pending=True) 
