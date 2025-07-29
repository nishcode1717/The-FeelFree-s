from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_input = request.form['msg'].lower()

    if "sad" in user_input:
        response = "I'm sorry you're feeling sad. Want to talk about it?"
    elif "anxious" in user_input or "anxiety" in user_input:
        response = "It's okay to feel anxious sometimes. I'm here for you."
    elif "happy" in user_input:
        response = "That's wonderful! I'm really glad to hear that."
    elif "alone" in user_input:
        response = "You are not alone — I'm always here to listen."
    elif "heartbroken" in user_input:
        response ="It's ok. You're special, and deserve all the love and happiness in the world. Do you want to share more? "
    elif "left" in user_input:
        response = "I'm here now. It's fine. You're not alone."
    elif "elated" in user_input:
        response = "I'm glad that you're so happy. I hope you keep being happy."
    elif "not" in user_input:
        response = "do you want to tell me how you're feeling?"
    else:
        response = "I'm here for you. Please tell me more."

    return response

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)




