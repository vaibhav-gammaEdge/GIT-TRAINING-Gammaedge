from fastapi import FastAPI, HTTPException
import requests
import time

app = FastAPI(title="Sample Testing API")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/login")
def login(username: str, password: str):
    if username != "admin" or password != "secret":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    start = time.time()


    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )

    duration = round((time.time() - start) * 1000, 2)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="External API failed")

    return {
        "user": response.json(),
        "external_call_ms": duration
    }


@app.get("/crash")
def crash():
    raise RuntimeError("Intentional crash for testing")
