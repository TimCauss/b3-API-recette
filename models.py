from pydantic import BaseModel, Field
from typing import List, Optional


class Ingredient(BaseModel):
    name: str
    quantity: str

class Recipe(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    steps: List[str]
    ingredients:  List[Ingredient]