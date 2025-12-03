# services/rounds.py

from .supa import supabase
from datetime import datetime

def start_round():
    """Crear una nueva ronda."""
    data = {
        "status": "betting",
        "start_time": datetime.utcnow().isoformat()
    }
    return supabase.table("rounds").insert(data).execute().data[0]


def get_current_round():
    """Última ronda creada."""
    res = supabase.table("rounds") \
        .select("*") \
        .order("start_time", desc=True) \
        .limit(1) \
        .execute()

    if res.data:
        return res.data[0]
    return None


def update_round(round_id, values):
    """Modificar ronda."""
    return supabase.table("rounds") \
        .update(values) \
        .eq("id", round_id) \
        .execute().data



