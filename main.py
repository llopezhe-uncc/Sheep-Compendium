from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

@app.get("/sheep/", response_model=list[Sheep])
def read_all_sheep():
    return db.get_all_sheep()

@app.post("/sheep", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    # Check if the sheep ID already exists to avoid duplicates
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    db.data[sheep.id] = sheep
    return sheep    # Return the newly added sheep data

@app.delete("/sheep/", response_model=Sheep)
def delete_sheep(id: int):
    sheep = db.get_sheep(id)

    if sheep is None:
        raise HTTPException(status_code=404, detail="Sheep with this ID does not exist")

    return db.delete_sheep(id)

@app.put("/sheep/{id}", response_model=Sheep)
def update_sheep(id: int, sheep: Sheep):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this ID does not exist")

    return db.update_sheep(id, sheep)