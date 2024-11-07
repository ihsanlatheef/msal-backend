import json
from fastapi import APIRouter, Depends, Security, Request
import logging
from auth import azure_scheme

logging.basicConfig(level=logging.INFO)

router = APIRouter(
    prefix="/api/users",
    responses={404: {"description":"Endpoint not found"}}
)

@router.get("/")
async def get_users(request: Request, user=Security(azure_scheme)):
    auth_header = request.headers.get("Authorization")
    
    if auth_header:
        token = auth_header.split(" ")[1]
        logging.info(f" Access Token: {token}")
    
    with open('./users/users.json', 'r', encoding='utf-8') as file_object:
        return json.load(file_object)