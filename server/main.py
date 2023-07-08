import uvicorn
from app.server import app

from dotenv import load_dotenv
from constants import *

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