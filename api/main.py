from fastapi import FastAPI
from models import Message
from steganography import encode_message, decode_message

app = FastAPI()


@app.post("/encode")
async def encode(message: Message):
    image_path = "C:/Users/balaj/Desktop/pexels-james-wheeler-1605325.jpg"  # Provide the path to your image file
    encoded_image = encode_message(image_path , message.text,)
    return encoded_image

@app.post("/decode")
async def decode():
    encoded_image_path = "../encodedimage/encoded.png"  # Provide the path to your encoded image file
    decoded_message = decode_message( encoded_image_path)
    return {"decoded_message": decoded_message}
