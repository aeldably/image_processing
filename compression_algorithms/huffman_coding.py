from .node import Node

from numpy import histogram, unique, sqrt, count_nonzero
from cv2 import imread, IMREAD_GRAYSCALE


class HuffmanCoding:
    def __init__(self, image_location):
        self.codes = dict()
        self.image_array = imread(image_location, IMREAD_GRAYSCALE)
        self.tree = list()

    def calculate_probability(self):
        """
        :return:
        """
        unique_values = unique(self.image_array)
        prob = histogram(self.image_array, unique_values)[0] / self.image_array.size

        return dict(zip(unique_values, prob))

    def make_node(self, ordered_prob):
        """
        :param ordered_prob:
        :return:
        """
        for pixel in ordered_prob.keys():
            node = Node(pixel=pixel,
                        prob=ordered_prob[pixel])
            self.tree.append(node)

    def add_codes(self, node, bin_value=''):
        """
        :param node:
        :param bin_value:
        :return:
        """
        new_bin_value = bin_value + str(node.code)

        if node.left:
            self.add_codes(node.left, new_bin_value)

        if node.right:
            self.add_codes(node.right, new_bin_value)

        if not node.left and not node.right:
            self.codes[node.pixel] = new_bin_value

    def calculate_rmse(self, image, compressed):
        """
        Calculates the Root Mean Squared Error

        :param image: original image in ndarray
        :param compressed: compressed image in ndarray
        :return: a float rmse value
        """
        image = image.flatten()
        compressed = compressed.flatten()

        return sqrt(((compressed - image)**2).mean())

    def total_gain(self):
        before_compression = self.image_array.size * 8
        after_compression = 0

        for pixel in self.codes.keys():
            count = count_nonzero(self.image_array == pixel)
            after_compression += count * len(self.codes[pixel])

        print("Space before compression: {} bits".format(before_compression))
        print("Space after compression: {} bits".format(after_compression))

    def get_encoded_output(self):
        encoded_output = list()
        for prob in self.codes.values():
            encoded_output.append(prob)

        encoded_output_str = ''.join([str(pixel_prob) for pixel_prob in encoded_output])

        return encoded_output_str

    def decode(self, encoded_output, huffman_tree):
        """
        :param encoded_output:
        :param huffman_tree:
        :return:
        """
        tree_head = huffman_tree
        decoded_output = list()
        for bin_value in encoded_output:
            if bin_value == '1':
                huffman_tree = huffman_tree.right
            elif bin_value == '0':
                huffman_tree = huffman_tree.left
            try:
                if huffman_tree.left.symbol is None and huffman_tree.right.symbol is None:
                    pass
            except AttributeError:
                decoded_output.append(huffman_tree.symbol)
                huffman_tree = tree_head
        decoded_output_str = ''.join([str(pixel_prob) for pixel_prob in decoded_output])

        return decoded_output_str

    def encode(self):
        """
        :return:
        """
        ordered_probabilities = self.calculate_probability()

        for pixel in ordered_probabilities.keys():
            node = Node(pixel=pixel,
                        prob=ordered_probabilities[pixel])
            self.tree.append(node)

        while len(self.tree) > 1:
            self.tree = sorted(self.tree, key=lambda x: x.prob)

            left_node = self.tree.pop(0)
            right_node = self.tree.pop(0)

            left_node.code = 0
            right_node.code = 1

            new_node = Node(pixel=left_node.pixel + right_node.pixel,
                            prob=left_node.prob + right_node.prob,
                            left=left_node,
                            right=right_node)

            self.tree.append(new_node)
            print(self.tree)

        # generate a list of huffman code for each pixel
        self.add_codes(node=self.tree[0])

        encoded_output_str = self.get_encoded_output()

        return encoded_output_str



