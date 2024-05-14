import uvicorn
from app.server import app
from constants import *
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware

load_dotenv(DOTENV_PATH)

def main():
    # TODO add envvars in prod
    uvicorn.run(
        app="app.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

if __name__ == '__main__':
    main()