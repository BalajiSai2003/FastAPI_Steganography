import cv2

def read_image(image_path):
    # sourcery skip: inline-immediately-returned-variable
    image = cv2.imread(image_path)
    return image

def save_image(image, save_path):
    cv2.imwrite(save_path, image)
