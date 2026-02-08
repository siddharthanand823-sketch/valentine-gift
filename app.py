import sys # Ye line zaroori hai logs dekhne ke liye
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # ---------------------------------------------------------
    # 👇 YAHAN USKA NAAM LIKH
    # ---------------------------------------------------------
    her_name = "Meri Jaan"
    # Note: Make sure aapki HTML file ka naam 'preview.html' hi ho
    return render_template('preview.html', name=her_name)

# 👇 YE NAYA CODE HAI - KHABRI (Spy)
@app.route('/she-said-yes')
def she_said_yes():
    # Jab wo button dabayegi, ye line Render ke logs mein chalegi
    print("LOG: 💖💖 BADHAI HO! USNE 'YES' DABA DIYA HAI! 💖💖", file=sys.stderr)
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
