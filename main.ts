basic.showLeds(`
    . # # # #
    # # . . #
    # # # # #
    # # # # #
    . # . . #
    `)
neZha.setMotorSpeed(neZha.MotorList.M1, -100)
basic.forever(function () {
    if (PlanetX_Basic.ultrasoundSensor(PlanetX_Basic.DigitalRJPin.J1, PlanetX_Basic.Distance_Unit_List.Distance_Unit_cm) < 40) {
        basic.pause(1000)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 50)
        neZha.setMotorSpeed(neZha.MotorList.M1, -48)
    } else if (PlanetX_Basic.ultrasoundSensor(PlanetX_Basic.DigitalRJPin.J2, PlanetX_Basic.Distance_Unit_List.Distance_Unit_cm) < 15) {
        basic.pause(1000)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 300)
    } else if (PlanetX_Basic.ultrasoundSensor(PlanetX_Basic.DigitalRJPin.J3, PlanetX_Basic.Distance_Unit_List.Distance_Unit_cm) < 15) {
        basic.pause(1000)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 50)
    } else {
        basic.pause(1000)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
    }
})
