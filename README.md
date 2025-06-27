# Bot-powered-with-AI
this telegram bot is mainly built off ai's. Currently there are vertexai and geminiai

# required modules: telebot, PIL, os, numpy, asyncio, google, vertex_ai_imagen and dotenv

Get ready because this is gonna be pretty long instruction...
# CREATE AND ACTIVATE TELEGRAM BOT
1. Go to telegram channel @BotFather
2. Generate your bot and copy it's token
3. In the line where is the variable bot insert your bots token

# DO NOT SHARE YOUR BOT TOKEN TO ANYBODY ELSE, IF THEY ARE ASKING FOR IT THEY ARE TRYING TO STEAL YOUR BOT AND USING AGAINST SOMETHING OFFENSIVE AND YOU'LL GET THE BLAME FOR IT
4. Anyways after inserting the bots token run the script
5. Find your bot in telegram through search option
6. And thats it for Telegram Bot itself..

# NOW LETS TUNE IN TO BOTH AI
1. Once you installed google module and have the gemini then head to the google platform https://ai.google.dev/
![2. Click on the explore models button](https://github.com/user-attachments/assets/fe3e94cb-f362-4c86-88e1-e3e639fb45ab)
![3. At the top right corner click on "Get Api Key"](https://github.com/user-attachments/assets/b56be7d4-23af-4d4b-a362-aa96a0ab8b65)
![4. Now click on create api key](https://github.com/user-attachments/assets/c5aca8d6-584d-41a7-b9e0-94cce89fe330)
![5. Copy your generated key](https://github.com/user-attachments/assets/28637b0f-247b-4464-befe-3a5879661427)
6. Create .env file and add there GEMAI_API variable and GEMAI_API="insert your gemini ai key"
7. Do the same thing with bot token (TOKEN="insert your bot token") 

# Now lets begin with vertex ai, its more complicated but it is alright (WARNING, vertex ai requires free trial along with your billing details. Make sure to turn off vertex ai key after you turn off your telegram bot
1. Go to https://console.cloud.google.com/
![2. Select and create a new project](https://github.com/user-attachments/assets/83a87940-94df-40fb-8f26-7c4181da7de0)
![3. select new project](https://github.com/user-attachments/assets/5f18443e-a9c4-4e23-b88d-6c6178a3e9be)
4. Give that project a name and use location "No Organisation"
![5. Go to api services and select credentials](https://github.com/user-attachments/assets/2e6a807a-380c-4e4e-b372-912a539409d7)
![6. Create service account key](https://github.com/user-attachments/assets/d392893e-8918-41f4-b160-ad8ac99d7766)
7. Click on your service account
![8. Click on the key tab and create a service account key](https://github.com/user-attachments/assets/39bad852-faf2-4b3d-acdf-595ba98c500b)
![9. Click add key](https://github.com/user-attachments/assets/2851c652-df8a-4dec-9b17-414341c25d78)
![10. Click create, select JSON and your generated key json file will be downloaded](https://github.com/user-attachments/assets/1836ac7e-4253-4566-8b42-5628aa59c328)
![11. Ensure that your json key is saved in your downloads](https://github.com/user-attachments/assets/541f1f4c-e105-41a5-8be6-78dd56726db6)
12. Add that json file to your project and copy the path with right mouse click on json file and copy the path AND paste it path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"HEREE"
13. Don't forget to add your billing details to that console google cloud platform or otherways it just will resist working.
14. Also in .env file create PROJECT_ID and enter your google console cloud project name
15. And now that's for the AI

# Later to this project I will add last three commands that are down below in the Script.
# ALSO DO NOT FORGET THAT IM NOT VERY ACTIVE HERE SO ASK CHATGPT, RESEARCH YOUR PROBLEMS. IF YOU DID SOMETHING WRONG IM NOT THE ONE WHO IS RESPONSIBLE
