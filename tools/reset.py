from datetime import datetime
from modules.scheduler import save_state
from modules.logger import log_info
    

def reset_limits():
    now = datetime.now()
    state = {
        'sent_today': [],
        'send_count': 0,
        'last_reset': now.date().strftime('%Y-%m-%d')
    }
    save_state(state)
    log_info("🛠️ Manual reset from terminal.")