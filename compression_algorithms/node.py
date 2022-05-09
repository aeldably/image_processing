class Node:
    def __init__(
            self,
            pixel,
            prob,
            left=None,
            right=None,
    ) -> None:
        """
        :param pixel:
        :param prob:
        :param left:
        :param right:
        """
        self.pixel = pixel
        self.prob = prob
        self.left = left
        self.right = right

        self.code = ''

    def __repr__(self):
        return '("%s", %s, %s, %s)' % (self.pixel, self.prob, self.left, self.right)
