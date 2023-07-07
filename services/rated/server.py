from flask import Flask
from flask_cors import CORS
from code import top_rated_blueprint

app = Flask(__name__)
CORS(app)
app.register_blueprint(top_rated_blueprint)

@app.route('/',methods=['GET'])
def top_func():
        return "Python Server ok"
        # Return the JSON response
        #return jsonify(json_response)

if __name__ == '__main__':
    app.run()