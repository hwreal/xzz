我的手 = 0

def on_gesture_shake():
    global 我的手
    我的手 = randint(1, 3)
    if 我的手 == 1:
        basic.show_leds("""
            # # . . #
            # # . # .
            # # # . .
            # # . # .
            # # . . #
            """)
    elif 我的手 == 2:
        basic.show_leds("""
            . . . . .
            . # # . .
            . # # . .
            . . . . .
            . . . . .
            """)
    else:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
