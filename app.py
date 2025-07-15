from flask import Flask, request, jsonify
import pickle, random

app = Flask(__name__)
model, intents = pickle.load(open("models/chatbot.pkl", "rb"))

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "Xin lỗi, bạn chưa nhập nội dung!"})
    tag = model.predict([user_input])[0]
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return jsonify({"response": random.choice(intent["responses"])})
    return jsonify({"response": "Em chưa hiểu ý anh/chị, mình hỏi lại giúp em nhé."})

if __name__ == "__main__":
    app.run(debug=True)
