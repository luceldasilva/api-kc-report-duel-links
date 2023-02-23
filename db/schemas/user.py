def user_schema(user) -> dict:
	return {"id": str(user["_id"]),
			"duelist": user["duelist"],
			"deck": user["deck"],
			"skill": user["skill"],
			"ndmax": user["ndmax"],
			"zerotg": user["zerotg"],
			"zephra": user["zephra"],
			"bryan": user["bryan"],
			}

def users_schema(users) -> list:
	return [user_schema(user) for user in users]