from flask import Flask, jsonify
app = Flask(__name__)



@app.route("/test")
def index():
    return 'Sample flask app'
if __name__ == '__main__':
    app.run()
