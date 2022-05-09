import cv2 as cv

from compression_algorithms.huffman_coding import HuffmanCoding

image_location = "images/8-bit-256-x-256-Grayscale-Lena-Image.png"

HF = HuffmanCoding(image_location=image_location)
print(HF.encode())
