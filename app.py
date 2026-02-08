from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # ---------------------------------------------------------
    # 👇 YAHAN USKA NAAM LIKH (Quotes "" ke andar)
    # ---------------------------------------------------------
    her_name = "Meri Jaan"  
    
    # Ye seedha surprise page kholega
    return render_template('preview.html', name=her_name)

if __name__ == '__main__':
    app.run(debug=True)