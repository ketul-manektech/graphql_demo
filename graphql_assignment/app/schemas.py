import uuid

from fastapi_users import schemas


class User_Info(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class Update_User(schemas.BaseUserUpdate):
    pass
