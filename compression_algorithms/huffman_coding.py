"""
 1. create a priority Queue Q consisting of each unique character
 
 """
import cv2 as cv
import json
from itertools import  zip_longest
import numpy as np
import matplotlib.pyplot as plt


class Node:

    def __init__(
                self,
                prob,
                pixel,
                left=None,
                right=None,
    ) -> None:
        """
        """
        self.left = left
        self.right = right
        self.pixel = pixel
        self.prob = prob

        self.code = ''

def calculate_probability(data):
    """
    The function calculates the probability for a given data.
    """
    pixels_prob = dict()
    for pixel in np.nditer(data):
        if pixels_prob.get(int(pixel)) is None:
            pixels_prob[int(pixel)] = (1 / 65536)
        else:
            pixels_prob[int(pixel)] += (1 / 65536)
    return pixels_prob

def calculate_codes(node, val=''):
    """

    :param node:
    :param val:
    :return:
    """
    newVal = val + str(node.code)

    if node.left:
        calculate_codes(node.left, newVal)
    if node.right:
        calculate_codes(node.right, newVal)

    if not node.left and not node.right:
        codes[node.pixel] = newVal

    return codes

"""
def add_missing_probabilities(pixels_prob):
    for pixel in range(256):
        if pixel not in pixels_prob.keys():
            pixels_prob[pixel] = 0
    return pixels_prob
"""

def output_encoding(img_data, huffman_encoding):
    """
    :param img_data:
    :param huffman_encoding:
    :return:
    """
    print(huffman_encoding)
    encoding_output = list()
    encoding_output = [code for code in huffman_encoding.values()]
    encoding_output_str = "".join(item for item in encoding_output)

    return encoding_output_str

def huffman_decoding(encoded_data, huffman_tree):
    decoded_upput = []
    for code in encoded_data:
        if code == 1:
            huffman_tree = huffman_tree.right
        elif code == 0:
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.pixel is None and huffman_tree.left.pixel is None:
                pass
        except AttributeError:
            decoded_upput.append(huffman_tree.pixel)
    string_code = "".join([code for code in decoded_upput])
    return string_code



def huffman_encoding(img_data):

    nodes = []

    for pixel in pixels_prob.keys():
        nodes.append(Node(pixels_prob.get(pixel), pixel))

    print(nodes)

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x:x.prob)

        # pick the smallest nodes
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        left.code = 1

        # combine the two nodes create a new one
        new_node = Node(left.prob+right.prob, left.pixel+right.pixel, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)
    he = calculate_codes(nodes[0])
    encoded_ouptut = output_encoding(img_data, he)

    return encoded_ouptut, nodes[0]



img = cv.imread("../images/8-bit-256-x-256-Grayscale-Lena-Image.png", cv.IMREAD_GRAYSCALE)
print(img.shape)


pixels_prob = calculate_probability(img)

print(pixels_prob)
codes = dict()
encoding, tree = huffman_encoding(img_data=pixels_prob)
print("encoding output", encoding)
print("decoded output", huffman_decoding(encoded_data=encoding, huffman_tree=tree))




