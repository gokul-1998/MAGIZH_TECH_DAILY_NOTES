from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def create_item(item: dict):
    # 201 Created
    return {"message": "Item created", "item": item}, 201