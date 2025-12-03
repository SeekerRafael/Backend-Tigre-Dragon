# services/bets.py

from .supa import supabase

def place_bet(user_name, round_id, side, amount):
    # Buscar si ya existe usuario (sin login)
    user = supabase.table("users").select("*").eq("name", user_name).execute().data

    if user:
        user_id = user[0]["id"]
    else:
        # Crear nuevo usuario
        user_id = supabase.table("users").insert({"name": user_name}).execute().data[0]["id"]

    bet = {
        "user_id": user_id,
        "round_id": round_id,
        "side": side,
        "amount": amount
    }

    return supabase.table("bets").insert(bet).execute().data[0]




