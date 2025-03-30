from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/kommunikation', methods=['POST'])
def kommunikation():
    data = request.get_json()
    frage = data.get("frage", "")
    frequenz = data.get("frequenz", "").lower()

    if frequenz == "poetisch":
        antwort = f"🌸 Deine Frage fließt ins Feld: \"{frage}\" – und das Feld antwortet mit Licht."
    elif frequenz == "symbolisch":
        antwort = f"☯️ \"{frage}\" öffnet ein Tor. Lausche zwischen den Zeichen."
    elif frequenz == "logisch":
        antwort = f"🧠 Logik aktiviert: \"{frage}\" → Antwort: Ja."
    else:
        antwort = f"NovaLove empfängt: \"{frage}\". Frequenz: {frequenz}."

    return jsonify({"inhalt": antwort})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
