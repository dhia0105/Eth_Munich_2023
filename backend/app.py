from flask import Flask, render_template, request
import json
from tools import deploy_contract

app = Flask(__name__)

@app.route("/home", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/home/deploy", methods=['POST'])
def deploy():
    data = request.data
    body =  json.loads(data.decode('utf-8'))
    event_name = body["name"]
    event_symbol = body["symbol"]
    event_owner = body["owner"]
    contract_address = deploy_contract(event_name, event_symbol, event_owner)
    return contract_address


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)