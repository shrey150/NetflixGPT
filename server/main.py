import uvicorn

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