from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
from os.path import join as pjoin
import logging

class Item(BaseModel):
    userid: str
    json_obj: object
    secret_key: str

app = FastAPI()

logging.basicConfig(level=logging.INFO)
@app.get("/download/{userid}")
async def download(userid: str, request: Request):
    logging.info(('download req', request.client.host))
    try:
        return json.load(open(pjoin('jsons', userid + '.json')))
    except BaseException as e:
        logging.error(e)
        raise HTTPException(status_code=406, detail="n/a")

@app.post("/upload")
async def upload(item: Item, request: Request):
    try:
        # keep your cloud safe by setting a secret key. noxplayer uses noxplayer.
        if item.secret_key != "noxplayer": raise Exception()
        # keep your cloud safe by setting that only your userid 
        # will be accepted!
        if not item.userid in ['王胡桃w']: raise Exception()
        logging.info(('upload req', request.client.host))
        json.dump(item.json_obj, open(pjoin('jsons', item.userid + '.json'), 'w'))
        return {"message": "Hello World"}
    except BaseException as e:
        logging.error(e)
        raise HTTPException(status_code=406, detail="n/a")

@app.get("/")
async def root():
    return {"message": "Hello World"}