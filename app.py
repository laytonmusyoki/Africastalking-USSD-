from flask import Flask, request, jsonify, render_template




app = Flask(__name__)




@app.route('/')
def initialize():
    pass


@app.route('/callback', methods=['POST'])
def callback():
    if request.method == 'POST':
        text=request.form['text']
        phone=request.form['phoneNumber']
        session_id=request.form['sessionId']
        print(text, phone, session_id)
        if text =="":
            res="CON Welcome to Mawazo Farmers\n"
            res +="1. Login\n"
            res +="2. Register"
            return res
        elif text =="1":
            res="CON Enter your phone number"
            return res
        elif text =="2":
            res="CON Enter your name"
            return res
        elif text.__contains__("1*"):
            res="END You are logged in"
            return res
        elif text.__contains__("2*"):
            res="END You are registered"
            return res
        return "END hello flask"








if __name__ == '__main__':
    app.run(debug=True)