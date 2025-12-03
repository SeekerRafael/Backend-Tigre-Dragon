

from datetime import datetime
from .rounds import get_current_round, update_round

def determine_winner_logic_only():
    rnd = get_current_round()
    if not rnd:
        return None

    tn = rnd["tiger_number"]
    dn = rnd["dragon_number"]

    if tn is None or dn is None:
        return None

    if tn > dn:
        winner = "tiger"
    elif dn > tn:
        winner = "dragon"
    else:
        winner = "tie"

    update_round(rnd["id"], {
        "winner": winner,
        "status": "finished",
        "end_time": datetime.utcnow().isoformat()
    })

    return winner

