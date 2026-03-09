import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Cargamos el .env que está una carpeta arriba
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(f"¡Hola {user}! Soy el bot de ShadowRoot.")

if __name__ == '__main__':
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    
    if not TOKEN:
        print("❌ Error: No se encontró el TELEGRAM_TOKEN")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("🚀 Bot básico encendido...")
        app.run_polling()

