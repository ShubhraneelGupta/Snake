from turtle import Turtle


INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.heading = RIGHT
        self.head.color("red")

    def turn(self, direc):
        if self.heading + 180 == direc or self.heading - 180 == direc:
            pass
        else:
            self.heading = direc
            self.head.seth(direc)

    def create_snake(self):
        for positions in INITIAL_POSITIONS:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("circle")
            new_segment.color("white")
            new_segment.goto(positions)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.penup()
        new_x = self.tail.xcor() - 20
        new_y = 0
        new_segment.goto(new_x, new_y)
        new_segment.shape("circle")
        self.segments.append(new_segment)

    def move(self):
        self.segments[-1].color("white")
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        self.turn(UP)

    def down(self):
        self.turn(DOWN)

    def right(self):
        self.turn(RIGHT)

    def left(self):
        self.turn(LEFT)