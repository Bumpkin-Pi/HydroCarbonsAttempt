from matplotlib import pyplot as plt

cos60 = 0.5
sin60 = 0.8660254


class Alkane:
    def up(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0]], [pen_pos[1], pen_pos[1] + 1])
        return [pen_pos[0], pen_pos[1] + 1]

    def down(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0]], [pen_pos[1], pen_pos[1] - 1])
        return [pen_pos[0], pen_pos[1] - 1]

    def upR(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0] + sin60], [pen_pos[1], pen_pos[1] + cos60])
        return [pen_pos[0] + sin60, pen_pos[1] + cos60]

    def upL(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0] - sin60], [pen_pos[1], pen_pos[1] + cos60])
        return [pen_pos[0] - sin60, pen_pos[1] + cos60]

    def downR(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0] + sin60], [pen_pos[1], pen_pos[1] - cos60])
        return [pen_pos[0] + sin60, pen_pos[1] - cos60]

    def downL(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0] - sin60], [pen_pos[1], pen_pos[1] - cos60])
        return [pen_pos[0] - sin60, pen_pos[1] - cos60]


class Alkene:
    def up(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0]], [pen_pos[1], pen_pos[1] + 1])
        return [pen_pos[0], pen_pos[1] + 1]

    def down(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0]], [pen_pos[1], pen_pos[1] - 1])
        return [pen_pos[0], pen_pos[1] - 1]

    def upR(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0] + sin60], [pen_pos[1], pen_pos[1] + cos60])
        return [pen_pos[0] + sin60, pen_pos[1] + cos60]

    def upL(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0] - sin60], [pen_pos[1], pen_pos[1] + cos60])
        return [pen_pos[0] - sin60, pen_pos[1] + cos60]

    def downR(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0] + sin60], [pen_pos[1], pen_pos[1] - cos60])
        return [pen_pos[0] + sin60, pen_pos[1] - cos60]

    def downL(self, pen_pos):
        plt.plot([pen_pos[0], pen_pos[0] - sin60], [pen_pos[1], pen_pos[1] - cos60])
        return [pen_pos[0] - sin60, pen_pos[1] - cos60]
