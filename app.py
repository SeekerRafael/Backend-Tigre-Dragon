# app.py

from flask import Flask, request, jsonify
from services.rounds import start_round, get_current_round
from services.bets import place_bet
from services.detect import detect_card, determine_winner

app = Flask(__name__)

# -------------------------
# RUTAS DEL JUEGO
# -------------------------

@app.post("/start_round")
def r_start():
    r = start_round()
    return jsonify(r)

@app.post("/bet")
def r_bet():
    data = request.json
    b = place_bet(
        data["user_name"],
        data["round_id"],
        data["side"],
        data["amount"]
    )
    return jsonify(b)

@app.post("/detect")
def r_detect():
    data = request.json
    result = detect_card(
        data["role"],     # 'tiger' o 'dragon'
        data["number"],
        data["color"]
    )
    return jsonify(result)

@app.post("/finish")
def r_finish():
    winner = determine_winner()
    return jsonify({"winner": winner})

@app.get("/state")
def r_state():
    rnd = get_current_round()
    return jsonify(rnd)

# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



