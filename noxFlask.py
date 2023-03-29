from flask import Flask, request, abort
import json
from os.path import join as pjoin
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/download', methods=['GET'])
def download():
    try:
        return json.load(open(pjoin('jsons', request.args.get('userid') + '.json')))
    except Exception as e:
        logging.error(e)
        print(e)
        abort(406)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = json.loads(request.data)
        if not data['secret_key']== 'noxplayer': 
            raise Exception("secret key invalid", data['secret_key'])
        if not data['userid'] in ['王胡桃w']: raise Exception('username invalid', data['userid'])
        json.dump(data['json_obj'], open(pjoin('jsons', data['userid'] + '.json'), 'w'))
        return "success."
    except Exception as e:
        logging.error(e)
        abort(406)
    
@app.route('/hi', methods=['GET'])
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port=6666)
    # gunicorn -w 2 'noxFlask:app' -b 0.0.0.0:6666