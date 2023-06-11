from fastapi import FastAPI
from pydantic import BaseModel
from steganography import encode_message, decode_message

app = FastAPI()

class Message(BaseModel):
    text: str
    password: str

@app.post("/encode")
def encode(message: Message):
    image_path = "path/to/image.png"  # Provide the path to your image file
    encoded_image_path = "path/to/encoded_image.png"  # Provide the path to save the encoded image
    encoded_image = encode_message(message.text, message.password, image_path)
    encoded_image.save(encoded_image_path)
    return {"message": "Message encoded successfully"}

@app.post("/decode")
def decode(password: str):
    encoded_image_path = "path/to/encoded_image.png"  # Provide the path to your encoded image file
    decoded_message = decode_message(password, encoded_image_path)
    return {"decoded_message": decoded_message}
