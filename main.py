from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 20000)}