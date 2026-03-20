import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import uvicorn


api =fastapi.FastAPI()
templates = Jinja2Templates(directory="templates")


@api.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request" : request})


if __name__ == "__main__":
    uvicorn.run(api, host='127.0.0.1', port=8000) 