import numpy as np
from Block import Block


class BlockHandler:
    def __init__(self):
        self.blocks = self.create_blocks()

    @staticmethod
    def create_blocks():
        colorrandom = list(np.random.choice(range(256), size=3))
        blocks = []
        for y in range(4):
            for x in range(0, 800, 80):
                blocks.append(Block(colorrandom, x + 4, 50 * (y + 1) + 2, 76, 25 - 2))
        return blocks



