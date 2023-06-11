# FastAPI_Steganography
Steganography application using FastAPI
### This application has 2 routes
## 1) encode
### This route responsible for hiding message in selected image path
## 2) decode
### This route responsible for extracting message from encoded image

# How to run locally


First, clone this repo by using the following command in cmd Make sure to have git and python3 installed
````

git clone https://github.com/BalajiSai2003/FastAPI_Steganography.git

````

Then, navigate to the cloned directory


````

cd FastAPI_Steganography

````

Then install fastapp using all flag like 

````

pip install -r requirements.txt

````

create a file named `.env` and write the following configuration in the file

````

image_path = path image in which you want to hide secret message
encoded_image_path = path where you what to store encoded image with name of the image with .png file format Example xyz/encodedImage.png

````

Then go this repo folder in your local computer run follwoing command
````

uvicorn main:app --reload

````

Then you can use following link to use the  API

````

http://127.0.0.1:8000/docs 

````
