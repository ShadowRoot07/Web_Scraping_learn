import os
import pytz
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Cargamos el .env que está una carpeta arriba
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

async def hora_vzla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    zona_vzla = pytz.timezone('America/Caracas')
    hora_actual = datetime.now(zona_vzla).strftime("%I:%M %p")
    await update.message.reply_text(f"🕒 Hola. En Venezuela son las: {hora_actual}")

async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    termino = " ".join(context.args)
    if not termino:
        await update.message.reply_text("❓ Por favor, escribe: /buscar [término].")
        return
    link = f"https://es.wikipedia.org/wiki/{termino.replace(' ', '_')}"
    await update.message.reply_text(f"📚 He buscado '{termino}' para su consulta.\n\nPuede leer más aquí: {link}")

async def ayuda_papa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = (
        "👨‍⚕️ **Asistente de Consulta v1.0**\n\n"
        "/hora - Ver la hora exacta en Venezuela.\n"
        "/buscar [tema] - Enlace rápido sobre un concepto."
    )
    await update.message.reply_text(mensaje, parse_mode='Markdown')

if __name__ == '__main__':
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    
    if not TOKEN:
        print("❌ Error: No se encontró el TELEGRAM_TOKEN")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", ayuda_papa))
        app.add_handler(CommandHandler("hora", hora_vzla))
        app.add_handler(CommandHandler("buscar", buscar))
        print("🚀 Asistente de psicología activo...")
        app.run_polling()

