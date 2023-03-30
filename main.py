from fastapi import FastAPI, HTTPException, Request, Header, Body
from typing import Annotated
from fastapi.responses import FileResponse
from os.path import join as pjoin
import logging
from urllib.parse import unquote


app = FastAPI()

logging.basicConfig(level=logging.INFO)
@app.get("/download/{userid}")
async def download(userid: str):
    try:
        return FileResponse(pjoin('jsons', userid + '.noxBackup'))
    except BaseException as e:
        logging.error(e)
        raise HTTPException(status_code=406, detail="n/a")

@app.post("/upload")
async def upload(
    request: Request,
    secret_key: Annotated[str | None, Header()] = None,
    userid: Annotated[str | None, Header()] = None):
    try:
        # keep your cloud safe by setting a secret key. noxplayer uses noxplayer.
        if secret_key != "noxplayer": raise Exception()
        username = unquote(userid)
        # keep your cloud safe by setting that only your userid 
        # will be accepted!
        if not username in ['王胡桃w']: raise Exception()
        with open(pjoin('jsons', username + '.noxBackup'), 'wb') as f:
            f.write(await request.body())
        return {"message": "Hello World"}
    except BaseException as e:
        logging.error(e)
        raise HTTPException(status_code=406, detail="n/a")

@app.get("/")
async def root():
    return {"message": "Hello World"}