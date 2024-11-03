from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for expenses and income records
data = {
    "expenses": [],
    "income": []
}

@app.route('/add_expense', methods=['POST'])
def add_expense():
    try:
        # Get data from the request
        expense = request.get_json()
        amount = expense.get("amount")
        description = expense.get("description", "")
        
        # Validate data
        if amount is None or amount <= 0:
            return jsonify({"error": "Amount must be a positive number"}), 400
        
        # Add expense record
        data["expenses"].append({
            "amount": amount,
            "description": description
        })
        
        return jsonify({"message": "Expense recorded", "data": data["expenses"]}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_income', methods=['POST'])
def add_income():
    try:
        # Get data from the request
        income = request.get_json()
        amount = income.get("amount")
        description = income.get("description", "")
        
        # Validate data
        if amount is None or amount <= 0:
            return jsonify({"error": "Amount must be a positive number"}), 400
        
        # Add income record
        data["income"].append({
            "amount": amount,
            "description": description
        })
        
        return jsonify({"message": "Income recorded", "data": data["income"]}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/data', methods=['GET'])
def get_data():
    # Endpoint to view recorded data
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
