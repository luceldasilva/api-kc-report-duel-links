from fastapi import FastAPI
from routers import kc_cup_feb_23

app = FastAPI()

@app.get("/")
async def root():
	return "ola k ase"


app.include_router(kc_cup_feb_23.kcfeb23)