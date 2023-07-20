from flask import Flask, request
from chatbot import ChatBot

app = Flask(__name__)

bot = ChatBot()

@app.route("/latest-message", methods=["GET"])
def get_latest_message():
    return {
        "is_generating": bot.is_generating(),
        "message": bot.get_latest_message(),
        "suggestions": bot.get_suggestions()
    }

@app.route("/send-message", methods=["POST"])
def send_message():
    message = request.json.get("message")
    bot.clear_context()
    bot.send_message(message)
    return {"status": "Message sent"}

@app.route("/clear-context", methods=["POST"])
def clear_context():
    bot.clear_context()
    return {"status": "Context cleared"}

@app.route("/start-driver", methods=["POST"])
def start_driver():
    p_b_cookie = request.json.get("p_b_cookie")
    bot_name = request.json.get("bot_name")
    bot.start_driver(p_b_cookie, bot_name)
    return {"status": "Driver started"}

@app.route("/kill-driver", methods=["POST"])
def kill_driver():
    bot.kill_driver()
    return {"status": "Driver killed"}

@app.route("/abort-message", methods=["POST"])
def abort_message():
    bot.abort_message()
    return {"status": "Message aborted"}

@app.route("/is-generating", methods=["GET"])
def is_generating():
    return {"is_generating": bot.is_generating()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)