import uvicorn

isOnProduction = False

# run with python3 index.py
if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0",
                port=8000, reload=not(isOnProduction))
