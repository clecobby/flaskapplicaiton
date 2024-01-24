from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

class HelloWorld:
    @router.get("/", summary="Returns a simple hello message")
    def get(self):
        """Returns a simple hello message."""
        return {"message": "Hello World!"}

app.include_router(router)

# If you want to run using uvicorn, you can use the following command:
# uvicorn app:app --host 0.0.0.0 --port 5000 --ssl-keyfile key.pem --ssl-certfile cert.pem
                                    