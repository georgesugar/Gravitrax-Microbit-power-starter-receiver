input.onButtonPressed(Button.A, function () {
    Launch_All_Balls(90)
})
function Launch_One_Ball (Angle: number) {
    Angle = 90
    Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo1, Angle)
    basic.pause(50)
    Angle = 100
    Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo1, Angle)
    return
}
function Launch_All_Balls (Angle: number) {
    Angle = 90
    Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo1, Angle)
    basic.pause(2000)
    Angle = 100
    Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo1, Angle)
    return
}
radio.onReceivedString(function (receivedString) {
    opperation = receivedString
    if (receivedString == "all") {
        Launch_All_Balls(90)
        basic.showIcon(IconNames.Happy)
    } else if (receivedString == "one") {
        Launch_One_Ball(90)
        basic.showIcon(IconNames.No)
    } else if (receivedString == "reset") {
        reset()
    } else {
    	
    }
})
input.onButtonPressed(Button.B, function () {
    Launch_One_Ball(90)
    basic.showIcon(IconNames.Happy)
})
function reset () {
    Angle = 100
    Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo1, Angle)
    basic.showString("R")
}
let opperation = ""
let Angle = 0
radio.setGroup(1)
Angle = 100
Kitronik_Robotics_Board.allOff()
Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo1, Angle)
let MyImageOne = images.createImage(`
    . . . . .
    . . . . .
    . . . . #
    . . . . .
    . . . . .
    `)
let myImageAll = images.createImage(`
    . . . . #
    . . . . #
    . . . . #
    . . . . #
    . . . . #
    `)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
	
})
