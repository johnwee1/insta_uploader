from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import instagrapi
import dotenv, os
import backend

dotenv.load_dotenv()
env = os.environ


cl = instagrapi.Client()
cl.login(env["USERNAME"], env["PASSWORD"])


class Message(BaseModel):
    name: str
    message: str


app = FastAPI()


@app.post("/send")
async def send(msg: Message):
    path = backend.build_image_pipeline(msg.name, msg.message)
    if not path:
        raise HTTPException(status_code=400, detail="I think your message was too edgy")
    cl.photo_upload(path, caption=f"this message was brough to you by {msg.name}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
