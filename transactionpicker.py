# Import Libraries
from flask import Flask, jsonify
from data import transactions_list



# Create Web App
app = Flask(__name__)


# returns list of transactions
@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    response = {'Transactions': transactions_list}
    return jsonify(response), 200




# Returns list of 10 transactions with highest fees
@app.route('/get_ten_highest_fees', methods=['GET'])
def get_ten_highest_fees():
    sorted_list = sorted(transactions_list, key=lambda x: x['Fee'], reverse=True)
    highest = []
    x = 0
    while x < 10:
        highest.append(sorted_list[x])
        x+= 1
    response = {'Ten highest fees:': highest}
    return jsonify(response), 200




# Returns list of 10 transactions with lowest fees
@app.route('/get_ten_lowest_fees', methods=['GET'])
def get_ten_lowest_fees():
    low = []
    sorted_list = sorted(transactions_list, key=lambda x: x['Fee'])
    x = 0
    while x < 10:
        low.append(sorted_list[x])
        x+= 1
    response = {'Ten lowest fees': low}
    return jsonify(response), 200


    


# Returns second highest total fee sum after picking 10 transactions
@app.route('/get_next_highest_total', methods=['GET'])
def get_next_highest_total():
    sorted_list = sorted(transactions_list, key=lambda x: x['Fee'], reverse=True)
    total = 0
    x = 0
    while x < 9:
        total+= sorted_list[x].get('Fee')
        x+= 1
    total += sorted_list[10].get('Fee')
    response = {'Next highest total:': total}
    return jsonify(response), 200
    



# Run app
app.run(host='0.0.0.0', port=5050)