from fastapi import FastAPI

app= FastAPI()


@app.get("/")
def home_page() -> dict[str, str]:
    return {"message":"Hello World"}

@app.get("/hello")
def hello_world():
    return {"message":"Hello Baxtiyor"}