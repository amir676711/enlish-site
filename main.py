import uvicorn
from api.api import create_app



def main():
    app = create_app()
    uvicorn.run(app,host="localhost",port=6000)

if __name__ == "__main__":
    main()