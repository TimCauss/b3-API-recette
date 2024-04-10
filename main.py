from typing import List
from fastapi import FastAPI, HTTPException
from models import Recipe

app = FastAPI()
recipes_db: List[Recipe] = []

err_not_found = "Recette non trouvée"

@app.get("/")
def read_root():
    return {"OK"}

@app.post("/recipes/")
def create_recipe(recipe: Recipe):
    recipe.id = len(recipes_db) + 1 
    recipes_db.append(recipe)
    return {"message":  "Recette créer avec succés.", "recipe": recipe}

@app.get("/recipes/", response_model=List[Recipe])
def read_recipes():
    return recipes_db

@app.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int):
    for recipe in recipes_db:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail=err_not_found)

@app.put("/recipes/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe_update: Recipe):
    for recipe in recipes_db:
        if recipe.id == recipe_id:
            recipe.title = recipe_update.title
            recipe.description = recipe_update.description
            recipe.steps = recipe_update.steps
            recipe.ingredients = recipe_update.ingredients
            return recipe
    raise HTTPException(status_code=404, detail=err_not_found)

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    for recipe in recipes_db:
        if recipe.id == recipe_id:
            recipes_db.remove(recipe)
            return {"message": "Recette supprimée avec succé"}
    raise HTTPException(status_code=404, detail=err_not_found)
