import telebot
#from keras.models import load_model
from PIL import Image, ImageOps
import os
import numpy as np
import asyncio
from google import genai
from vertex_ai_imagen import ImagenClient
from dotenv import load_dotenv

load_dotenv()
GEN_API = os.environ.get("GEMAI_API")
TOKEN = os.environ.get("BOT_API")
PROJECT_ID = os.environ.get("PROJECT_ID")
path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"direction for your google service account key"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm your new telegram bot. Use command /info for additional commands that could be used.")
    
@bot.message_handler(commands=['info'])
def send_possible_commands(message):
    bot.reply_to(message, """* /about command is for explanation for global warming.\n
    * /solution is to find a solution for global warming disaster and type with that command your
    prompt that will be an additional prompt from you.\n
    * /generateimg is a command to generate image, after the command enter your prompt
    for example (/generateimg global warming around the earth)
    """)
    
    
@bot.message_handler(commands=['about']) # what is global warming
def globalWarming_defin(message):
    bot.reply_to(message, "Global warming is a disaster 🌍🔥. It makes the Earth hotter because of gases like carbon dioxide from cars and factories 🚗🏭. This causes ice to melt 🧊➡️💧, sea levels to rise 🌊, and weather to become worse 🌪️☀️. To stop it, we should use clean energy 🌞💨, plant trees 🌳, and save water 💧. If we act now, we can protect our planet for the future 🌎❤️.")
    
@bot.message_handler(commands=['solution']) # how we can decrease global warming situations
def globalWarming_solution(message):
    user_prompt = message.text.replace("/solution ", "")
    client = genai.Client(api_key=GEN_API)
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""Solution for decreasing global warming disasters,
        Write solution for each individual person and make it easy to understand
        and a short text no need for any complex words with emojis.
        Additional Prompt from user: {user_prompt}""",
    )
    bot.reply_to(message, response.text)
    
@bot.message_handler(commands=['generateimg']) # to generate image with ai
def globalWarming_solution(message):
    user_prompt = message.text.replace("/generateimg ", "")
    client = ImagenClient(project_id=PROJECT_ID)
    client.setup_credentials(path)
    
    if not user_prompt:
        bot.reply_to(message, "❗Your input is empty. Please type something after /generateimg")
        return

    bot.reply_to(message, "🖼️ Generating image for you, please wait...")

    async def run_generation():
        return await client.generate(
            prompt=user_prompt,
            aspect_ratio="16:9"
        )

    try:
        image_result = asyncio.run(run_generation())
    except RuntimeError:
        # This handles case where an event loop is already running (e.g. in some IDEs)
        loop = asyncio.get_event_loop()
        image_result = loop.run_until_complete(run_generation())

    # ✅ Save the image directly (not subscriptable)
    image_result.save("tempo.png")

    with open("tempo.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=f"✅ Here is your image for:\n'{user_prompt}'")
        
#@bot.message_handler(commands=['askquestion']) # ask quiz from ai
#def globalWarming_solution(message):
    
#@bot.message_handler(commands=['dialogue']) # enter a dialogue with ai
#def globalWarming_solution(message): 
    
#@bot.message_handler(commands=['telegramGame']) # play game from telegram
#def globalWarming_solution(message):                      
        
bot.polling()