# api/api2.py
from fastapi import Depends
from utils import create_api, get_api_key

app = create_api()

@app.get("/inference", dependencies=[Depends(get_api_key)])
def read_api2():
    return {"message": "This is API 2"}
