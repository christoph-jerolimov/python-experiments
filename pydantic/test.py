from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    labels: dict[str, str]


external_data = {
    "id": 123,
    "name": "Joe Doe",
    "labels": {
        "action movies": "yes",
    },
}

user = User.model_validate(external_data)

print(user)
print(user.model_dump())
print(user.model_dump_json())
