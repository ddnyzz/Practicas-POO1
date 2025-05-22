## ejemplo uso de flask
# ##27/03/25

from flask import Flask

app = Flask(__name__)

ALLOWED_IP = ['10.2.80.117']

@app.before_request
def limit_remote_addr():
    if request.remote_addr not in ALLOWED_IP:
        abort(403)
        
@app.route('/')
def hola_mundo():
    return "Hola mundo Flask"

if __name__ == '__main__':
    app.run(host='10.2.80.28', port=5000)
    
