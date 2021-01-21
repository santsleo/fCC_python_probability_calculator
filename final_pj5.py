import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, ball_amount):
        if ball_amount < len(self.contents):
            balls = random.sample(self.contents, ball_amount)
            for ball in balls:
                self.contents.remove(ball)
            return balls
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    desired_events = 0
    for i in range(num_experiments):
        exp_hat = copy.deepcopy(hat)
        balls = exp_hat.draw(num_balls_drawn)
        complies = True
        for key, value in expected_balls.items():
            if balls.count(key) < value:
                complies = False
        if complies:
            desired_events += 1
    probability = desired_events / num_experiments
    return probability


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)
