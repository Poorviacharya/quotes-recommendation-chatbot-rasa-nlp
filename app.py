from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.json.get("message")
    
    # Send to Rasa REST API
    rasa_response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": user_message}
    )
    
    return jsonify(rasa_response.json())

if __name__ == "__main__":
    app.run(port=8000, debug=True)