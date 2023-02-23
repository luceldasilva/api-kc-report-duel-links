from fastapi import APIRouter, HTTPException, status
from db.models.users import User, UserUpdate
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from pymongo.collection import ReturnDocument

kcfeb23 = APIRouter(prefix="/kcfeb23",
					tags=["kcfeb23"],
					responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado :'v"}})
	

def search_user(duelist: int):
	try:
		user = db_client.users.find_one({"duelist": duelist})
		return User(**user_schema(user))
	except:
		return {"error": "No está el usuario Kappa"}


@kcfeb23.get("/", response_model=list[User])
async def users():
	return users_schema(db_client.users.find())


@kcfeb23.get("/{duelist}")
async def user(duelist: int):
	return search_user(duelist)


@kcfeb23.post("/", response_model=User, status_code=status.HTTP_201_CREATED) 
async def user(user: User):
	if type(search_user(user.duelist)) == User:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ey, el usuario ya existe")
	
	user_dict = dict(user)
	del user_dict["id"]
	
	id = db_client.users.insert_one(user_dict).inserted_id 
	new_user = user_schema(db_client.users.find_one({"_id":id}))
	return User(**new_user)


@kcfeb23.delete("/{duelist}", status_code=status.HTTP_204_NO_CONTENT)
async def user(duelist: int):
	
	found = db_client.users.find_one_and_delete({"duelist": duelist})
	
	if not found: 
		raise HTTPException(status_code=404, detail="El usuario no existe")


@kcfeb23.patch("/", response_model=User)
async def user(user: UserUpdate):
	
	if not type(search_user(user.duelist)) == User:
		raise HTTPException(status_code=404, detail="Ese usuario no existe")
	
	user_dict = dict(user)
	del user_dict["id"]
	
	try:		
		db_client.users.find_one_and_update(
			{"duelist": user.duelist}, {"$set": user.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
	except:
		return {"error": "No se ha actualizado el usuario"}
	
	return search_user(user.duelist)