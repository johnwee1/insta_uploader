from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import instagrapi
import dotenv, os
import backend

dotenv.load_dotenv("secrets/.env")
env = os.environ


cl = instagrapi.Client()
cl.login(env["USERNAME"], env["PASSWORD"])


class Message(BaseModel):
    name: str
    message: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/send")
async def send(msg: Message):
    path = backend.build_image_pipeline(msg.name, msg.message)
    if not path:
        raise HTTPException(status_code=400, detail="Either message too edgy or name too long (what are you trying to do?)")
    cl.photo_upload(path, caption=f"this message was brough to you by {msg.name}")

@app.get("/health")
def read_health():
    return {"status": "UP"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
