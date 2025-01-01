from pydantic import BaseModel


class TokenModel(BaseModel):
    access_token: str
    token_type: str


class TokenDataModel(BaseModel):
    username: str | None = None


class UserModel(BaseModel):
    username: str
    role: str
    name: str
    email: str


class UserInDBModel(UserModel):
    hashed_password: str


class PurchasesModel(BaseModel):
    id: int
    item: str
    price: int


class ReportsModel(BaseModel):
    id: int
    title: str
    status: str


class UserDataModel(BaseModel):
    name: str
    email: str
    purchases: list[PurchasesModel]


class UserResponseModel(BaseModel):
    message: str
    data: UserDataModel


class AdminDataModel(BaseModel):
    name: str
    email: str
    reports: list[ReportsModel]


class AdminResponseModel(BaseModel):
    message: str
    data: AdminDataModel
