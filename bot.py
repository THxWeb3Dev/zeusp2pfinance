import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask
from threading import Thread
import os

# --- CONFIGURAÇÃO DE CREDENCIAIS ---
# Seu Token (Já configurado)
TOKEN = "8590639855:AAG4F62QVn2ljYiLaGA3G_vJtA4Fko7yHVk"

# Seu ID de Admin (Para referência ou logs futuros)
ADMIN_ID = 6719823918

# ⚠️ IMPORTANTE: Cole aqui o link do seu site no GitHub Pages
# Exemplo: "https://seu-usuario.github.io/zeus-p2p"
APP_URL = "https://thxweb3dev.github.io/zeusp2pfinance" 

# Inicializa o Bot
bot = telebot.TeleBot(TOKEN)

# --- SERVIDOR WEB PARA MANTER O BOT ONLINE 24H (NO RENDER) ---
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
    user_first_name = message.from_user.first_name
    
    # Texto da mensagem de boas-vindas
    texto = (
        f"⚡ <b>Olá, {user_first_name}!</b>\n\n"
        "Seja bem-vindo ao <b>ZEUS⚡️P2P | Finance</b>.\n\n"
        "Somos o futuro das finanças descentralizadas. "
        
        "Realize Depósitos, Cobranças e Saques via PIX. Pague Faturas e faça Saques via Cripto. Pague Boletos de até R$ 20.000,00 sem burocracias e sem KYC.\n\n"
        
        "👇 <b>Clique abaixo para acessar o App:</b>"
    )

    # Criação do botão que abre o Mini App
    markup = InlineKeyboardMarkup()
    # O botão WebApp precisa de HTTPS (GitHub Pages fornece isso)
    botao_app = InlineKeyboardButton(text="📱 Acessar Gateway | Banking", web_app=WebAppInfo(url=APP_URL))
    markup.add(botao_app)

    # Envia a mensagem
    bot.send_message(message.chat.id, texto, parse_mode="HTML", reply_markup=markup)

    # (Opcional) Log no console do servidor quando alguém entra
    print(f"🚀 Acesso de: {user_first_name} (ID: {message.from_user.id})")

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    keep_alive() # Inicia o servidor web invisível
    bot.infinity_polling() # Inicia o bot do Telegram
