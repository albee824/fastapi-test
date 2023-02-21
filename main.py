from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/calc/double/{num}")
def read_item(num: int):
    return {"num": num, "answer": num * 2}
