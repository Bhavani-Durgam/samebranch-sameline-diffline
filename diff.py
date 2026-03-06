from flask import Flask
app = Flask(__name_Bhavani_)
@app.route("/")
def home(): return "Hello World"
app.run()
