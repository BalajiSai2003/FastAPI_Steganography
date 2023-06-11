from PIL import Image
import os
import numpy as np 
def encode_message(image_path, message, encoded_image_path):
    """
    Encodes a message into an image using the LSB technique.
    """
    # Open image and convert to RGB format
    img = Image.open(os.path.join(image_path)).convert('RGB')
    # Convert image to numpy array
    img_array = np.array(img)
    # Get image dimensions
    height, width, channels = img_array.shape
    # Convert message to binary
    message_bin = ''.join(format(ord(c), '08b') for c in message)
    # Add end of message delimiter
    message_bin += '1111111111111110'
    # Get the maximum number of bits to encode
    max_bits = height * width * channels // 8
    if len(message_bin) > max_bits:
        raise ValueError('Message is too large to encode in image.')
    # Convert message length to binary and pad with zeros
    message_length = format(len(message_bin), '016b')
    # Add message length to the beginning of the binary message
    message_bin = message_length + message_bin
    # Iterate over each pixel in the image
    index = 0
    for row in range(height):
        for col in range(width):
            for channel in range(channels):
                pixel_value = img_array[row, col, channel]
                if index < len(message_bin):
                    # Get the least significant bit of the pixel value
                    pixel_bin = format(pixel_value, '08b')[:-1] + message_bin[index]
                    # Convert new pixel value back to integer
                    new_pixel_value = int(pixel_bin, 2)
                    # Modify pixel value
                    img_array[row, col, channel] = new_pixel_value
                    index += 1
                else:
                    break
            else:
                continue
            break
        else:
            continue
        break
    # Convert numpy array back to image
    img_encoded = Image.fromarray(img_array)
    # Save the encoded image
    img_encoded.save( encoded_image_path)
    return {"message": "Message encoded successfully", "image_path":  encoded_image_path}


def decode_message(image_path):
    """
    Decodes a message from an image using the LSB technique.
    """
    # Open image and convert to RGB format
    img = Image.open(os.path.join(image_path)).convert('RGB')
    # Convert image to numpy array
    img_array = np.array(img)
    # Get image dimensions
    height, width, channels = img_array.shape
    path = os.path.join(image_path)  
    os.remove(path)
    # Iterate over each pixel in the image
    message_bin = ''
    for row in range(height):
        for col in range(width):
            for channel in range(channels):
                pixel_value = img_array[row, col, channel]
                # Get the least significant bit of the pixel value
                pixel_bin = format(pixel_value, '08b')[-1]
                # Append least significant bit to message binary string
                message_bin += pixel_bin
                # Check if message delimiter is found
                if message_bin[-16:] == '1111111111111110':
                    # Extract message length from binary string
                    message_length = int(message_bin[:16], 2)
                    # Extract message from binary string
                    message_bin = message_bin[16:message_length+16]
                    # Convert binary message back to text
                    message = ''.join(chr(int(message_bin[i:i+8], 2)) for i in range(0, len(message_bin), 8))
                    return message