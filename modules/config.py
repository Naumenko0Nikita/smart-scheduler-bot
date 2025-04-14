import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
SESSION_NAME = os.getenv("SESSION_NAME")
TARGET_CHAT = int(os.getenv("TARGET_CHAT"))
SCHEDULE_FILE = os.getenv("SCHEDULE_FILE")

schedule = [
    {
        "day": 2,  
        "time": "17:30",
        "message": '''Вітаю, шановні колеги❗️

✅Нагадую що о 19:30 починається заняття за темою "Frontend"

⚠️Приєднуйтесь без запізнень за посиланням нижче! ⚠️

Зустрінемось на уроці.👍

Посилання на зустріч, основне:

https://meet.jit.si/Group_Python_WEB_12_00

Посилання на зустріч, резервне:

https://meet.google.com/cjr-nzmb-wrz
'''
    },
    {
        "day": 5,  
        "time": "10:00",
        "message": '''👋 Вітаю, шановні колеги!

🕛 Нагадую, що сьогодні о 12:00 розпочнеться заняття на тему:
📘 "Backend"

⚠️ Будь ласка, приєднуйтеся вчасно, використовуючи основне посилання!
Той хто не поставив лайк той жукандос! 
🔗 Основне посилання на зустріч:
meet.jit.si/Group_Python_WEB_12_00

🔗 Резервне посилання (у разі потреби):
meet.google.com/cjr-nzmb-wrz

📚 Чекаємо вас на уроці!
'''
    },
    {
        "day": 0,  
        "time": "15:10",
        "message": "TEST"
    },
]
