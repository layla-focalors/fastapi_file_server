# from typing import Annotated
from fastapi import *
from fastapi import staticfiles
from fastapi.responses import FileResponse
import os
import uvicorn
import uuid 
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pymysql
import os
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# os.chdir('/home/work/Cycle-GAN-summer2Winter/pix2pix/app-server/fastapi-server-upload')
os.chdir('/home/work/Cycle-GAN-summer2Winter/pix2pix/app-server/fastapi-server-upload')

templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = {
    "https://localhost:12540",
    "http://localhost",
    "https://127.0.0.1:12540",
    "http://127.0.0.1:12540",
    "http://127.0.0.1",
    "https://proxy1.nipa2023.ktcloud.com:10483/proxy/12540/?",
    "https://proxy1.nipa2023.ktcloud.com:10483/proxy/12540",
}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/upload_video")
async def upload_video(file: UploadFile):
    UPLOAD_DIR = "./video"
    content = await file.read()
    filename = f"{str(uuid.uuid4())}.mp4"
    # filename = "video.mp4"
    with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
        fp.write(content) 
    return {"filename": filename}

@app.get("/download/video/{video_id}")
async def download_video(file: FileResponse, video_id: str): 
    return FileResponse(f'./video/{video_id}.mp4')

@app.get('/process/{video_id}')
async def process_video(video_id: str):
    os.system('echo is working')
    return "waiting progress"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=12640)
# dev : junhyeok seo : GIT SAVED