# services/detect.py

from datetime import datetime
from .rounds import get_current_round, update_round


# ============================================================
# DETECTAR CARTA (TIGRE o DRAGON)
# ============================================================

def detect_card(role, number, color):
    """
    Guarda número y color según el rol recibido ('tiger' o 'dragon').
    Avanza estado: betting → detecting.
    """
    rnd = get_current_round()
    if not rnd:
        return {"error": "no_round"}

    values = {}

    if role == "tiger":
        values["tiger_number"] = number
        values["tiger_color"] = color

    elif role == "dragon":
        values["dragon_number"] = number
        values["dragon_color"] = color

    else:
        return {"error": "invalid_role"}

    # Si está en betting, la detección cambia a detecting
    if rnd["status"] == "betting":
        values["status"] = "detecting"

    update_round(rnd["id"], values)
    return values


# ============================================================
# DETERMINAR GANADOR
# ============================================================

def determine_winner():
    """
    Compara TIGER vs DRAGON y decide quién ganó.
    También actualiza la ronda a 'finished'.
    """
    rnd = get_current_round()
    if not rnd:
        return {"error": "no_round"}

    tn = rnd.get("tiger_number")
    dn = rnd.get("dragon_number")

    # Si faltan números, no se puede decidir
    if tn is None or dn is None:
        return {"error": "missing_values"}

    if tn > dn:
        winner = "tiger"
    elif dn > tn:
        winner = "dragon"
    else:
        winner = "tie"

    update_round(
        rnd["id"],
        {
            "winner": winner,
            "status": "finished",
            "end_time": datetime.utcnow().isoformat()
        }
    )

    return {"winner": winner}
