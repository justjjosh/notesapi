from fastapi import FastAPI
from routers import notes, tags

app = FastAPI(title="Notes API", version="1.0.0")

app.include_router(notes.router)
app.include_router(tags.router)

@app.get("/")
def root():
    return {"message": "Welcome to Notes API"}