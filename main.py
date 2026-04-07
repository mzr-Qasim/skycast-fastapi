import fastapi
# from pathlib import Path
# import json
from dotenv import load_dotenv
from starlette.staticfiles import StaticFiles
import uvicorn
from services import openweather_service
from views import home
from api import weather_api
import os
# from fastapi.middleware.cors import CORSMiddleware


api = fastapi.FastAPI()


# api.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # <- You can replace "*" with specific origins for production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



def configure():
    configure_routing()
    configure_api_keys()
    
load_dotenv()
print("OPENWEATHER_API_KEY:", os.getenv("OPENWEATHER_API_KEY"))

def configure_api_keys():
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise Exception("API key not found. Set OPENWEATHER_API_KEY environment variable.")

    openweather_service.api_key = api_key



def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)      




if __name__ == "__main__":
    configure()
    uvicorn.run(api, host='127.0.0.1', port=8000) 
else:
    configure()