from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home() -> dict[str, str]:
    return {"data": "message"}


@app.get("/contacts")
async def contacts() -> int:
    return 34


posts = [
    {'id': 1, 'title': 'News1', 'body': 'text1'},
]


def main(x):
    x = x ** 2
    return x


if __name__ == "__main__":
    print(main(5))
