from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from auth import azure_scheme
from users import users

app = app = FastAPI(
    swagger_ui_oauth2_redirect_url='/oauth2-redirect',
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': 'ac8b13f6-e535-420f-b319-2f2e1e6c3cad',
        'scopes': 'https://testmsalintegration.onmicrosoft.com/auth-backend/access_as_user',
    },
)

app.add_middleware(CORSMiddleware, 
                   allow_origins=["http://localhost:5173"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.get("/")
def read_root():
    return {"message": "This is the index route for fastapi"}

app.include_router(users.router, dependencies=[Security(azure_scheme)])

