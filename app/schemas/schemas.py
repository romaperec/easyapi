from pydantic import BaseModel, Field
from typing import Annotated

class UserAddSchema(BaseModel):
    name: Annotated[str, Field(max_length=20)]
    description: Annotated[str, Field(max_length=150)] | None = "I love easyapi :)"