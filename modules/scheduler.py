import os
import json
import asyncio
from datetime import datetime
from .config import schedule, TARGET_CHAT
from .messenger import send_message
from .logger import log_info, log_error



STATE_FILE = 'state.json'

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            state = json.load(f)
            state['sent_today'] = set(tuple(key) for key in state['sent_today'])
            return state
    return {'sent_today': set(), 'send_count': 0, 'last_reset': None}


def save_state(state):
    state['sent_today'] = [tuple(key) for key in state['sent_today']]
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

async def schedule_loop():
    state = load_state()  
    sent_today = state['sent_today']
    send_count = state['send_count']
    last_reset = state['last_reset']
    
    MAX_MESSAGES_PER_DAY = 10
    now = datetime.now()
    current_time = now.strftime('%H:%M')  
    weekday = now.weekday()
    if last_reset != now.date().strftime('%Y-%m-%d'):
        last_reset = now.date().strftime('%Y-%m-%d')
        sent_today.clear()
        send_count = 0
        log_info("🔄 Reset daily limits.")
   
        state = {'sent_today': list(sent_today), 'send_count': send_count, 'last_reset': last_reset}
        save_state(state)

    for task in schedule:
        key = (weekday, task["time"], task["message"])
        if (task["day"] == weekday and 
            task["time"] == current_time and 
            key not in sent_today and 
            send_count < MAX_MESSAGES_PER_DAY):

            try:
                await send_message(TARGET_CHAT, task["message"])
                log_info(f"\n✅ Message sent: '{task['message']}' to '{TARGET_CHAT}'\n")
                sent_today.add(key)  
                send_count += 1
                print(send_count)
                state = {'sent_today': list(sent_today), 'send_count': send_count, 'last_reset': last_reset}
                save_state(state)

            except Exception as ex:
                log_error(f"\n❌ Error sending message '{task['message']}' to '{TARGET_CHAT}': {str(ex)}\n")

    await asyncio.sleep(30)
