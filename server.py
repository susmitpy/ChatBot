# curl -X POST http://54.70.136.179:5555 -d "text=Hey&message=Hello"
# curl -X GET http://54.70.136.179:5555?message=HeyThere

from flask import Flask,request,jsonify

app=Flask(__name__)
token='Token'
# app.route
# def


@app.route('/', methods=["GET"])
def index():
    print(request.args)
    query = request.args.get('query')
    if query == 'token':
        response = {'key':token}
    else:
        response = {'text': 'Hey There'}
    return jsonify(response)


@app.route('/',methods=['POST'])
def post():
    print(request.form)
    req_token = request.form.get('token')
    if req_token == token:
        response = {'reply' : "Verified"}
    else:
        response = {'reply' : "Wrong token"}
    return jsonify(response)


if __name__ == '__main__':
    app.run()