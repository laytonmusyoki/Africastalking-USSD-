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
        elif text =="1*1":
            res="CON Options available\n"
            res +="1. View products\n"
            res +="2. View orders\n"
            res +="3. Check balance \n"
            res +="4. Withdraw funds\n"
            res +="5. Logout"
            return res
        elif text =="1*1*1":
            res="END Products available\n"
            res +="1. Maize\n"
            res +="2. Beans\n"
            res +="3. Potatoes\n"
            res +="4. Tomatoes\n"
            res +="5. Cabbage"
            return res
        elif text =="1*1*2":
            res="END Orders\n"
            res +="1. Layton's order\n"
            res +="2. James' order\n"
            res +="3. Davids' order\n"
            res +="4. Justins' order \n"
            return res
        elif text =="1*1*3":
            res="END Your balance is Ksh 5000"
            return res
        elif text =="1*1*4":
            res="CON Enter amount to withdraw"
            return res
        elif text=="1*1*5":
            res="END You have been logged out"
            return res
        elif text.__contains__("2*"):
            res="END You are registered"
            return res
        return "END hello flask"




if __name__ == '__main__':
    app.run(debug=True)