import draw
import matplotlib.pyplot as plt

#plt.plot([10, -15], [-10, 15], color="white")

cos60 = 0.5  # up
sin60 = 0.866025403784  # right
Alkane = draw.Alkane()
pen_pos = [-5, 0]


class Hex:
    p1, p2, p3, p4, p5, p6 = [[""] * 3] * 6
    pos = [0, 0]

    def __init__(self, points, pos):
        self.p1, self.p2, self.p3, self.p4, self.p5, self.p6 = points
        self.pos = pos

    def change_structure(self, points):
        self.p1, self.p2, self.p3, self.p4, self.p5, self.p6 = points

    def draw1(self, _pen_pos):
        if self.p1[0] == "c":
            Alkane.upL(_pen_pos)
        else:
            print("functional group")

        if self.p1[1] == "c":
            Alkane.upR(_pen_pos)
        else:
            print("functional group")

        if self.p1[2] == "c":
            Alkane.down(_pen_pos)
        else:
            print("functional group")

    def draw2(self, _pen_pos):
        if self.p2[0] == "c":
            Alkane.up(_pen_pos)
        else:
            print("functional group")

        if self.p2[1] == "c":
            Alkane.downR(_pen_pos)
        else:
            print("functional group")

        if self.p2[2] == "c":
            Alkane.downL(_pen_pos)
        else:
            print("functional group")

    def draw3(self, _pen_pos):
        if self.p3[0] == "c":
            Alkane.upR(_pen_pos)
        else:
            print("functional group")

        if self.p3[1] == "c":
            Alkane.down(_pen_pos)
        else:
            print("functional group")

        if self.p3[2] == "c":
            Alkane.upL(_pen_pos)
        else:
            print("functional group")

    def draw4(self, _pen_pos):
        if self.p4[0] == "c":
            Alkane.downR(_pen_pos)
        else:
            print("functional group")

        if self.p4[1] == "c":
            Alkane.downL(_pen_pos)
        else:
            print("functional group")

        if self.p4[2] == "c":
            Alkane.up(_pen_pos)
        else:
            print("functional group")

    def draw5(self, _pen_pos):
        if self.p5[0] == "c":
            Alkane.down(_pen_pos)
        else:
            print("functional group")

        if self.p5[1] == "c":
            Alkane.upL(_pen_pos)
        else:
            print("functional group")

        if self.p5[2] == "c":
            Alkane.upR(_pen_pos)
        else:
            print("functional group")

    def draw6(self, _pen_pos):
        if self.p6[0] == "c":
            Alkane.downL(_pen_pos)
        else:
            print("functional group")

        if self.p6[1] == "c":
            Alkane.up(_pen_pos)
        else:
            print("functional group")

        if self.p6[2] == "c":
            Alkane.downR(_pen_pos)
        else:
            print("functional group")

    def draw(self):
        _pen_pos = self.pos
        self.draw1(_pen_pos)
        _pen_pos[1] -= 1
        self.draw2(_pen_pos)
        _pen_pos[1] -= cos60
        _pen_pos[0] -= sin60
        self.draw3(_pen_pos)
        _pen_pos[1] += cos60
        _pen_pos[0] -= sin60
        self.draw4(_pen_pos)
        _pen_pos[1] += 1
        self.draw5(_pen_pos)
        _pen_pos[1] += cos60
        _pen_pos[0] += sin60
        self.draw6(_pen_pos)


hexagon = Hex([["c", "", ""], ["", "", ""], [""] * 3, [""] * 3, [""] * 3, ["c", "", ""]], [0, 0])

hexagons = []  # [[Hex([[""]*3]*6, [0, 0])]*5]*5
for x in range(10):
    tmp = []
    for y in range(10):
        tmp.append(Hex([[""] * 3] * 6, [(2 * sin60 * x) - 10, 15 - (3 * y)]))
    hexagons.append(tmp)

hexagons[5][4].change_structure([["c", "", ""], ["", "", ""], [""] * 3, [""] * 3, ["c", "", ""], ["c", "", ""]])
hexagons[4][4].change_structure([["c", "", ""], ["", "", ""], ["c", "c", ""], [""] * 3, ["", "", "c"], ["", "", ""]])
hexagons[4][5].change_structure([["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["c", "", ""]])
hexagons[6][4].change_structure([["", "", "c"], ["", "", "c"], ["", "", "c"], ["", "", "c"], ["", "", "c"], ["", "c", "c"]])
hexagons[4][3].change_structure([["", "", ""], ["", "", ""], ["", "c", "c"], ["", "", ""], ["", "", ""], ["", "", ""]])
hexagons[3][4].change_structure([["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "c", "c"]])
hexagons[3][3].change_structure([["", "", ""], ["", "", ""], ["c", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]])
hexagons[6][3].change_structure([["", "", ""], ["", "", "c"], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]])


#hexagons[4][5].change_structure([["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]])




for x in range(len(hexagons)):
    for y in range(len(hexagons[x])):
        hexagons[x][y].draw()


plt.axis('equal')
plt.show()
