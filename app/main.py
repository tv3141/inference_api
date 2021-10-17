import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile

from app import config
from app import inference


app = FastAPI()


@app.post("/predict")
def predict(image: UploadFile = File(...)):
    print(image.content_type)
    label = inference.infer(image.file)
    return {"response": label}


def run_app():
    uvicorn.run(
        "app.main:app",
        host=config.HOST,
        port=config.PORT,
        log_level="info",
        reload=True,
        reload_dirs=['app']
    )
