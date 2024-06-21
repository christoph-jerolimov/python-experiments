from fastapi import FastAPI
from fastapi_cli.cli import main
from typing import Any

app = FastAPI()

movies = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]


@app.get("/")
def home() -> str:
    return "hello world\n"


@app.get("/movies")
def get_all_movies() -> list[Any]:
    return movies


@app.get("/movies/{index}")
def get_movie_by_index(index: int) -> Any:
    return movies[index]


if __name__ == "__main__":
    main()
