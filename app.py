from flask import Flask, request, jsonify, render_template,session
import pymysql




app = Flask(__name__)

app.secret_key = 'mawazo'


connection=pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='ussd',
                            )




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
            res="CON Enter your password"
            return res
        elif text =="2":
            res="CON Enter your password"
            return res
        elif text.__contains__("1*"):
            password = text.split("*")[1]
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE password=%s", (password,))
            user = cursor.fetchone()
            cursor.close()
            if user:
                session['user_id']=user[0]
                res="CON Options available\n"
                res +="1. View products\n"
                res +="2. View orders\n"
                res +="3. Check balance \n"
                res +="4. Withdraw funds\n"
                res +="5. Logout"
                return res
            else:
                res="END invalid password\n"
                return res
        elif text.__contains__("1*1"):
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
            session.pop('user_id', None)
            res="END You have been logged out"
            return res
        elif text.__contains__("2*"):
            password = text.split("*")[1]
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE password=%s", (password,))
            user = cursor.fetchone()
            if user:
                res="END You are already registered"
                return res
            else:
                cursor.execute("INSERT INTO users (password) VALUES (%s)", (password,))
                connection.commit()
                cursor.close()
                res="END You have been registered"
                return res

        return "END hello flask"




if __name__ == '__main__':
    app.run(debug=True)