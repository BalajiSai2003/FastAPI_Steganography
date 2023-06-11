import cv2
import numpy as np

def encode_message(message, password, image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is valid
    if image is None:
        raise ValueError("Invalid image file")

    # Convert the message to binary representation
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Generate the encryption key based on the password
    np.random.seed(sum(ord(char) for char in password))
    key = np.random.randint(0, 256, size=len(binary_message))

    # Encode the binary message into the image pixels
    encoded_image = np.copy(image)
    for i, bit in enumerate(binary_message):
        row = i // image.shape[1]
        col = i % image.shape[1]
        if bit == '1':
            encoded_image[row, col] = np.bitwise_or(image[row, col], 1)
        else:
            encoded_image[row, col] = np.bitwise_and(image[row, col], 254)

    # Apply the encryption key to the encoded image
    encoded_image ^= key.reshape(image.shape)

    return encoded_image


def decode_message(password, image_path):
    pass