def on_button_pressed_a():
    Launch_All_Balls(90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def Launch_One_Ball(Angle: number):
    Angle = 90
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, Angle)
    basic.pause(50)
    Angle = 100
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, Angle)
    return
def Launch_All_Balls(Angle2: number):
    Angle2 = 90
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, Angle2)
    basic.pause(2000)
    Angle2 = 100
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, Angle2)
    return

def on_received_string(receivedString):
    global opperation
    opperation = receivedString
    if receivedString == "all":
        Launch_All_Balls(90)
        basic.show_icon(IconNames.HAPPY)
    elif receivedString == "one":
        Launch_One_Ball(90)
        basic.show_icon(IconNames.NO)
    elif receivedString == "reset":
        reset()
    else:
        pass
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    Launch_One_Ball(90)
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.B, on_button_pressed_b)

def reset():
    global Angle3
    Angle3 = 100
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, Angle3)
    basic.show_string("R")
opperation = ""
Angle3 = 0
radio.set_group(1)
Angle3 = 100
Kitronik_Robotics_Board.all_off()
Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, Angle3)
MyImageOne = images.create_image("""
    . . . . .
    . . . . .
    . . . . #
    . . . . .
    . . . . .
    """)
myImageAll = images.create_image("""
    . . . . #
    . . . . #
    . . . . #
    . . . . #
    . . . . #
    """)
basic.show_icon(IconNames.ANGRY)

def on_forever():
    pass
basic.forever(on_forever)

def on_in_background():
    while True:
        basic.pause(100)
        if opperation == "all":
            myImageAll.scroll_image(1, 200)
        elif opperation == "one":
            MyImageOne.scroll_image(1, 200)
        basic.show_string(opperation)
control.in_background(on_in_background)
