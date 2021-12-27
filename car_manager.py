import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE

        # self.create_car()

    # 1.a to create the list of cars
    def create_car(self):
        # Every time, the chance of creating a new car is 1/6

        random_num = random.randint(1, 6)
        if random_num == 1:
            car = t.Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_cor = random.randrange(-250, 250, 10)
            car.goto(300, y_cor)
            self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT * 0.5

