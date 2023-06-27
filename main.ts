let 我的手势 = 0
input.onGesture(Gesture.Shake, function () {
    我的手势 = randint(1, 3)
    if (我的手势 == 1) {
        basic.showLeds(`
            # # . . #
            # # . # .
            # # # . .
            # # . # .
            # # . . #
            `)
    } else if (我的手势 == 2) {
        basic.showLeds(`
            . . . . .
            . # # . .
            . # # . .
            . . . . .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    }
})
