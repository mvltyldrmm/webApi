from flask import Flask,jsonify
import json

app = Flask(__name__)
veri1 ={
    "ad": "Jane",
    "soyad": "Doe",
    "hobiler": ["running", "sky diving", "singing"],
    "yas": 25,
    "egitim": [
        {
            "lisans": "itu",
                        "bolum": "Bilgisayar muhendisligi",
            "not": 3.08
        },
        {
            "yukseklisans": "Gazi universitesi",
                        "bolum": "bilisim Sistemleri",
            "not": 3.45
        }
    ]
}

@app.route('/',methods=['GET'])
def hello():
    return "hello world"



@app.route('/listele',methods=['GET'])
def yazdir():
    return veri1


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

