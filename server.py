from flask import Flask,request,jsonify
from werkzeug.datastructures import ImmutableMultiDict


app=Flask(__name__)




if __name__ == '__main__':
  app.run()