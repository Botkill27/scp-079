basic.show_leds("""
    . # # # #
    # # . . #
    # # # # #
    # # # # #
    . # . . #
    """)
neZha.set_motor_speed(neZha.MotorList.M1, -100)

def on_forever():
    if PlanetX_Basic.ultrasound_sensor(PlanetX_Basic.DigitalRJPin.J1,
        PlanetX_Basic.Distance_Unit_List.DISTANCE_UNIT_CM) < 40:
        basic.pause(1000)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 50)
        neZha.set_motor_speed(neZha.MotorList.M1, -48)
    elif PlanetX_Basic.ultrasound_sensor(PlanetX_Basic.DigitalRJPin.J2,
        PlanetX_Basic.Distance_Unit_List.DISTANCE_UNIT_CM) < 15:
        basic.pause(1000)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 300)
    elif PlanetX_Basic.ultrasound_sensor(PlanetX_Basic.DigitalRJPin.J3,
        PlanetX_Basic.Distance_Unit_List.DISTANCE_UNIT_CM) < 15:
        basic.pause(1000)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 50)
    else:
        basic.pause(1000)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
basic.forever(on_forever)
