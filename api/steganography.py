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
    # sourcery skip: inline-immediately-returned-variable
    # Read the encoded image
    encoded_image = cv2.imread(image_path)

    # Check if the image is valid
    if encoded_image is None:
        raise ValueError("Invalid image file")

    # Generate the decryption key based on the password
    np.random.seed(sum(ord(char) for char in password))
    key = np.random.randint(0, 256, size=encoded_image.size)

    # Apply the decryption key to the encoded image
    decoded_image = encoded_image ^ key.reshape(encoded_image.shape)

    binary_message = ''.join(
        '1' if pixel % 2 == 1 else '0' for pixel in decoded_image.reshape(-1)
    )
    # Convert the binary message to text
    decoded_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

    return decoded_message