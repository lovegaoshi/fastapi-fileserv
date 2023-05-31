from fastapi import FastAPI, Response, HTTPException, Request
import os
from urllib.parse import unquote
import vercelsql

app = FastAPI()

@app.get("/download/{userid}")
async def download(userid: str):
    try:
        return Response(content=vercelsql.get(userid))
    except:
        raise HTTPException(status_code=406, detail="n/a")

@app.post("/upload")
async def upload(
    request: Request,
    secret_key,
    userid):
    try:
        if secret_key is None: secret_key = request.headers.get('secret-key')
        if userid is None: userid = request.headers.get('userid')
        # keep your cloud safe by setting a secret key. noxplayer uses noxplayer.
        if secret_key != "noxplayer": raise Exception('wrong key')
        username = unquote(userid)
        # keep your cloud safe by setting that only your userid 
        # will be accepted!
        if not username in os.environ['USERID'].split(','): raise Exception('wrong user')
        vercelsql.save(username, bytes(await request.body()))
        return {"message": "Hello World"}
    except:
        raise HTTPException(status_code=406, detail="n/a")

@app.get("/")
async def root():
    return {"message": "noxbackup is available"}
