from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World!"}
    return {"message": "hihi, this is my v first line."}
