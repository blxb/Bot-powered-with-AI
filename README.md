# 🤖 Bot-powered-with-AI

This telegram bot is mainly built off AI's. Currently there are VertexAI and GeminiAI ✨🤝

# 📦 Required modules: telebot, PIL, os, numpy, asyncio, google, vertex_ai_imagen, dotenv

## ⚠️ Get ready because this is a pretty long instruction...

# 🚀 CREATE AND ACTIVATE TELEGRAM BOT

1. 💬 Go to telegram channel [@BotFather]

2. 🔑 Generate your bot and copy its token

3. 📝 Insert your bot's token in the variable line where bot is defined

## ⚠️ DO NOT SHARE YOUR BOT TOKEN to anybody else. If they are asking for it, they are trying to steal your bot and use it offensively, and you’ll get the blame for it.

4. ▶️ After inserting the bot token, run the script

5. 🔍 Find your bot in telegram through the search option

6. ✅ That’s it for the Telegram Bot itself.

## 🤖 NOW LET'S TUNE IN TO BOTH AI

1. 📡 Once you installed google module and have Gemini, head to: https://ai.google.dev/

2. 🖱️ Click on the explore models button
![](https://github.com/user-attachments/assets/fe3e94cb-f362-4c86-88e1-e3e639fb45ab)
3. 🗝️ At the top right corner click on "Get API Key"
![](https://github.com/user-attachments/assets/b56be7d4-23af-4d4b-a362-aa96a0ab8b65)

4. 🆕 Click on create API key
![](https://github.com/user-attachments/assets/c5aca8d6-584d-41a7-b9e0-94cce89fe330)

5. 📋 Copy your generated key
![](https://github.com/user-attachments/assets/28637b0f-247b-4464-befe-3a5879661427)

6. 📝 Create .env file and add GEMAI_API variable: GEMAI_API="insert your Gemini AI key"

7. Do the same with bot token: TOKEN="insert your bot token"

# ☁️ NOW LET'S BEGIN WITH VERTEX AI

## ⚠️ (WARNING: Vertex AI requires a free trial and your billing details. Turn off Vertex AI key after turning off your Telegram bot)

1. 🌐 Go to https://console.cloud.google.com/

2. ➕ Select and create a new project
![](https://github.com/user-attachments/assets/83a87940-94df-40fb-8f26-7c4181da7de0)

3. 🆕 Select new project
![](https://github.com/user-attachments/assets/5f18443e-a9c4-4e23-b88d-6c6178a3e9be)

4. 🏷️ Give that project a name, use location "No Organisation"

5. ⚙️ Go to API services and select credentials
![](https://github.com/user-attachments/assets/2e6a807a-380c-4e4e-b372-912a539409d7)

6. 🗝️ Create service account key
![](https://github.com/user-attachments/assets/d392893e-8918-41f4-b160-ad8ac99d7766)

7. 👤 Click on your service account

8. 🔑 Click on the key tab and create a service account key
[](https://github.com/user-attachments/assets/39bad852-faf2-4b3d-acdf-595ba98c500b)

9. ➕ Click add key
![](https://github.com/user-attachments/assets/2851c652-df8a-4dec-9b17-414341c25d78)

10. 📥 Click create, select JSON, and your generated key json file will be downloaded
![](https://github.com/user-attachments/assets/1836ac7e-4253-4566-8b42-5628aa59c328)

11. 💾 Ensure your JSON key is saved in your downloads
![](https://github.com/user-attachments/assets/541f1f4c-e105-41a5-8be6-78dd56726db6)

12. 📝 Add that JSON file to your project. Copy its path (right click ➔ copy path) and paste it in:
path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"HERE"

13. 💳 Don’t forget to add your billing details in Google Cloud Console, otherwise it will not work.

14. 📝 Also in .env file, create PROJECT_ID and enter your Google Cloud project name.

## ✅ And that's it for the AI setup!

# 🛠️ Later to this project I will add last three commands shown below in the Script.

# ⚠️ ALSO DO NOT FORGET: I'm not very active here, so ask ChatGPT or research your problems. If you did something wrong, I am not responsible.
