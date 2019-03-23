from flask import Flask,request,jsonify
# from werkzeug.datastructures import ImmutableMultiDict


app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Good Susmit</h1>"




if __name__ == '__main__':
  app.run()