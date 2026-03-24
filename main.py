import fastapi
from pathlib import Path
import json
from starlette.staticfiles import StaticFiles
import uvicorn
from services import openweather_service
from views import home
from api import weather_api


api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()
    

def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print (f"Warning: file {file} does not exist, you cannot continue without it.")
        raise Exception("settings.json file not found, you cannot continue without it.")
    
    with open('settings.json') as file:
        settings = json.load(file)
        openweather_service.api_key = settings.get('api_key')



def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)      




if __name__ == "__main__":
    configure()
    uvicorn.run(api, host='127.0.0.1', port=8000) 
else:
    configure()