from fastapi import FastAPI
from routes.permits import router as permits_router


app = FastAPI(title="Buja Portal API Platform", version="1.0.0")


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(permits_router, prefix="/api/v1", tags=["Permits"])