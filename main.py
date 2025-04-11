from random import random

from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 127.0.0.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}