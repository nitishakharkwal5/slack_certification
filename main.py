from fastapi import FastAPI

app = FastAPI()


@app.post("/items/")
async def create_item(item):
    return item
