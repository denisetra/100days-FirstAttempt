
from turtle import Screen
import time, random
from frame import outside_frame
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My_Frogger(Turtle version)")
outside_frame()
screen.tracer(0)
sleep_time = [.1, .2, .3, .4, .05]

my_player = Player()
car_num = 0
car_manager = CarManager()
my_score = Scoreboard()

screen.listen()  ## listen for keystrokes
screen.onkey(my_player.up,"Up")
screen.onkey(my_player.left, "Left")
screen.onkey(my_player.right, "Right")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    my_score.display_score()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(my_player) < 20:
            game_is_on = False
            my_score.game_over()

    # Detect a successful crossing
    if my_player.is_at_finish_line():
        my_player.go_to_start()
        car_manager.level_up()
        my_score.increase_score()



screen.exitonclick()







