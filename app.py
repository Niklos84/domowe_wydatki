from flask import Flask, jsonify, abort, make_response, Response, request
from models import finance

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_key"

@app.route("/finance/", methods=["GET"])
def finance_list():
    return jsonify(finance.all())

@app.route("/finance/total/", methods=["GET"])
def finance_total():
    total = 0
    for i in finance.all():
        total += float(i['amount'])
    return jsonify(total)

@app.route("/finance/<int:finance_id>", methods=["GET"])
def get_finance(finance_id):
    finance_record = finance.get(finance_id)
    if not finance_record:
        abort(404)
    return jsonify({"finance_record": finance_record})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.route("/finance/", methods=["POST"])
def create_finance_record():
    if not request.json or not 'date' in request.json:
        abort(400)
    new_record = {
        'id': finance.all()[-1]['id'] + 1,
        'date': request.json['date'],
        'category': request.json['category'],
        'description': request.json.get('description', ""),
        'amount': request.json['amount']
    }
    finance.create(new_record)
    return Response(status=201)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route("/finance/<int:finance_id>", methods=['DELETE'])
def delete_finance_record(finance_id):
    result = finance.delete(finance_id)
    if not result:
        abort(404)
    return Response(status=200)

@app.route("/finance/<int:finance_id>", methods=["PUT"])
def update_finance_record(finance_id):
    record = finance.get(finance_id)
    if not record:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'date' in data and not isinstance(data.get('date'), str),
        'category' in data and not isinstance(data.get('category'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'amount' in data and not isinstance(data.get('amount'), str)
    ]):
        abort(400)
    updated_record = {
        'id': data.get('id', record['id']),
        'date': data.get('date', record['date']),
        'category': data.get('category', record['category']),
        'description': data.get('description', record['description']),
        'amount': data.get('amount', record['amount'])
    }
    finance.update(finance_id, updated_record)
    return jsonify({'record': updated_record})

if __name__ == "__main__":
    app.run(debug=True)