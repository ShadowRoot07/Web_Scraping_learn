import os
import datetime
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Cargamos el .env que está una carpeta arriba
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 ¡Hola! Soy tu asistente personal.\nUsa /ayuda.")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ahora = datetime.datetime.now().strftime("%H:%M:%S del %d/%m/%Y")
    mensaje = f"🤖 **Estado**\n📅 Hora: {ahora}\n🚀 Servidor: Termux"
    await update.message.reply_text(mensaje, parse_mode='Markdown')

async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🌐 Ver mi Repo", url="https://github.com/ShadowRoot07/Web_Scraping_learn")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Acceso directo al código:', reply_markup=reply_markup)

if __name__ == '__main__':
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    
    if not TOKEN:
        print("❌ Error: No se encontró el TELEGRAM_TOKEN")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("ayuda", info))
        app.add_handler(CommandHandler("repo", github))
        print("🚀 Bot Pro encendido...")
        app.run_polling()

