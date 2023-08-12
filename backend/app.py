from flask import Flask, render_template, request, jsonify
import json
from tools import deploy_contract, add_to_registred, verify_blacklisted

app = Flask(__name__, static_folder="./static")

@app.route("/home", methods=['GET'])
def home():
    return render_template('event_index.html')

@app.route("/home/deploy", methods=['POST'])
def deploy():
    data = request.data
    body =  json.loads(data.decode('utf-8'))
    event_name = body["eventName"]
    event_symbol = body["eventSymbol"]
    event_owner = body["eventAddress"]
    contract_address = deploy_contract(event_name, event_symbol, event_owner)
    return jsonify({"contract_address":contract_address})

@app.route("/event/apply/<eventname>", methods=['GET'])
def register_applicant(eventname):
    return render_template('applicant_index.html', eventname=eventname)

@app.route("/event/apply", methods=['POST'])
def apply_event():
    #event_name= request.args.get('eventname')
    data = request.data
    body =  json.loads(data.decode('utf-8'))
    email_address = body["emailAddress"]
    wallet_applicant = body["walletApplicant"]
    event_name = body["eventName"]
    blacklisted = verify_blacklisted(event_name, wallet_applicant)
    if not blacklisted:
        registred = add_to_registred(event_name, wallet_applicant, email_address)
    return jsonify({"Registred":registred})


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)