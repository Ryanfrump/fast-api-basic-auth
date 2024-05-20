from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app= FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
async def get_token(request_form: OAuth2PasswordRequestForm = Depends()):
    print(f"Here is the request form : {request_form}")
    return {"access_token": "some_token_that_i_think_is_neat", "token_type": "bearer"}

@app.get("/test")
async def get_something(token: str = Depends(oauth_scheme)):
    return {"message": "you did it!", "token": token}