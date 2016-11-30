from turtle import *


class DrawFigureWithTurtle(Turtle):
    def __init__(self, aShapeType):
        Turtle.__init__(self, shape="classic")
        self.edgeNumber = aShapeType
        self.angle = 360 / self.edgeNumber
        self.lineLength = aShapeType * 10

    def _change_start_position(self):
        penup()
        setpos(self.xPos, self.yPos)
        pendown()

    def _goto_home_position(self):
        penup()
        home()
        pendown()

    def _draw_with_turtle(self):
        self._change_start_position()

        loop_counter = 0

        while loop_counter < self.edgeNumber:
            forward(self.lineLength)
            right(self.angle)
            loop_counter += 1

        self._goto_home_position()

    def draw_figure(self, aXPos, aYPos):
        self.xPos = aXPos
        self.yPos = aYPos

        self._draw_with_turtle()

Triangle = DrawFigureWithTurtle(3)
Triangle.draw_figure(-100, 100)

Square = DrawFigureWithTurtle(4)
Square.draw_figure(0, 100)

Pentagon = DrawFigureWithTurtle(5)
Pentagon.draw_figure(100, 100)

Hexagon = DrawFigureWithTurtle(6)
Hexagon.draw_figure(-100, -50)

Octagon = DrawFigureWithTurtle(8)
Octagon.draw_figure(100, -50)
