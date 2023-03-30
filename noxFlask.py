from flask import Flask, request, abort, send_file
from os.path import join as pjoin
import logging
from urllib.parse import unquote

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/download/<userid>', methods=['GET'])
def download(userid):
    try:
        return send_file(pjoin('jsons', userid + '.noxBackup'), mimetype="application/gzip")
    except Exception as e:
        logging.error(e)
        abort(406)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if not request.headers['secret-key']== 'noxplayer': 
            raise Exception("secret key invalid", request.headers['secret_key'])
        username = unquote(request.headers['userid'])
        if not username in ['王胡桃w']: raise Exception('username invalid', username)
        with open(pjoin('jsons', username + '.noxBackup'), 'wb') as f:
            f.write(request.data)
        return "success."
    except Exception as e:
        logging.error(e)
        abort(406)
    
@app.route('/', methods=['GET'])
def hello():
    return "noxbackup flask is up"

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=6666, debug=True)
    # gunicorn -w 2 'noxFlask:app' -b 0.0.0.0:9527
