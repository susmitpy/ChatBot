from flask import Flask,request,jsonify
import requests

app=Flask(__name__)
token='Token'
url = "http://numbersapi.com/"
# app.route
# def


@app.route('/webhook', methods=["POST"])
def api():
    req = request.get_json(silent=True, force=True)  # Standard
  #  print(req)  # Prints full details
    params = req["queryResult"]['parameters']
    type_var = params.get('type')
    num_var = params.get('number-integer')
    print("Type: " + type_var)
    print("Number: " + str(num_var))
    target = url+str(int(num_var))+'/'+str(type_var)
    print("Target URL: " + target)
    res = requests.get(target)
    ans = res.text
    response = {
        "fulfillmentText": ans
    }
    return jsonify(response)




if __name__ == '__main__':
    app.run()