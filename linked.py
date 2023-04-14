from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json['message'] # Get the message from the client
    reply = generate_reply(message) # Generate a reply for the message

    return jsonify({'reply': reply})

def generate_reply(message):
    return "Hello, I am a chatbot!"

if __name__ == '__main__':
    app.run()
