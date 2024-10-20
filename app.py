from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# A simple function to generate bot responses
def generate_response(user_message):
    # Simple rule-based responses for demonstration purposes
    if "hello" in user_message.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_message.lower():
        return "I'm just a bot, but I'm doing great!"
    elif "bye" in user_message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Can you rephrase?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = generate_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7212)
