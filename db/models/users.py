from pydantic import BaseModel
from datetime import datetime, timedelta
from pytz import timezone
from typing import Optional

now = datetime.now(timezone('America/Eirunepe'))
yesterday = now - timedelta(days=1)


'''
Cuando Deta tenga 3.11 pondré el | None
:(
'''


class User(BaseModel):
	id: Optional[str]
	duelist: int
	deck: str
	skill: str
	ndmax = yesterday.strftime('%d-%m-%Y')
	zerotg: Optional[bool] = False
	zephra: Optional[bool] = False
	bryan: Optional[bool] = False


class UserUpdate(BaseModel):
	id: Optional[str]
	duelist: int
	deck: Optional[str] = None
	skill: Optional[str] = None
	ndmax: Optional[str] = None
	zerotg: Optional[bool] = None
	zephra: Optional[bool] = None
	bryan: Optional[bool] = None