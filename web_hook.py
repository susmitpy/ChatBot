from flask import Flask,request,jsonify

app=Flask(__name__)
token='Token'
# app.route
# def


@app.route('/webhook', methods=["POST"])
def api():
    req = request.get_json(silent=True, force=True)  # Standard
    print(req)
    print(request.form)
    response = {
        "fulfillmentText": "WebHook Called"
    }
    return jsonify(response)




if __name__ == '__main__':
    app.run()