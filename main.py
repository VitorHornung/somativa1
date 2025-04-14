from random import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
def read_root():
    return {"Olá, DevOps!!"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}