
import code

class Node:

    def __init__(
        self,
        symbol,
        prob,
        left=None,
        right=None,
        ) -> None:
        """
        """
        self.left = left
        self.right = right
        self.symbol = symbol
        self.prob = prob

        self.code = ''


def calculate_probability(data):
    """
    The function calculates the probability for a given data.
    """
    pixels_prob = dict()
    for pixel in data:
        if pixels_prob.get(pixel) is None:
            pixels_prob[pixel] = 1/256
        else:
            pixels_prob[pixel] += 1/256
    return pixels_prob

codes = dict()

def calculate_codes(node, val=''):

    newVal = val + str(node.code)

    if node.left:
        calculate_codes(node.left, newVal)
    if node.right:
        calculate_codes(node.right, newVal)
    
    if not node.left and not node.right:
        codes[node.symbol] = newVal

    return codes

def output_encoded(data, coding):
    encoding_output = list()

    for c in data:
        print(coding[c], end = '')
        encoding_output.append(coding[c])
    
    string = ''.join([str(item) for item in encoding_output])

    return string

def total_gain(data, coding):
    before_compression = len(data) * 8

    after_compression = 0
    symbols = coding.keys()

    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])
    print("Space usage before compression (in bits): ", before_compression)
    print("Space usage after compression (in bits):", after_compression)
