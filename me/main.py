from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

fake_secret_token = "testenvtoken"

fake_db = {
    1: {"id": 1, "name": "Running", "length": 60},
    2: {"id": 2, "name": "Muay Thai", "length": 75}
}

app = FastAPI()


class Exercise(BaseModel):
    id: int
    name: str
    length: int


@app.get("/exercises/{exercise_id}")
def read_exercises(exercise_id: int, x_token: Annotated[str, Header()]):
    if x_token == fake_secret_token:
        return fake_db[exercise_id]

    return {"exercise_id": exercise_id}


@app.post("/exercises/")
def create_exercise(exercise: Exercise, x_token: Annotated[str, Header()]):
    if x_token == fake_secret_token:
        fake_db[exercise.id] = exercise
        return fake_db[exercise.id]

    return exercise
