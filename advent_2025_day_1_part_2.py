def countZeros(rotations):
    dialPosition = 50
    totalZeros = 0
    for rotation in rotations:
        passThroughZero = 0
        direction = rotation[0]
        clicks = rotation[1:]
        clicks = int(clicks)
        passThroughZero += clicks//100
        clicks = clicks%100

        if direction == 'L':
            clicks *= -1

        isInitZero = dialPosition==0
        dialPosition += clicks

        if dialPosition > 99:
            dialPosition -= 100
            if(dialPosition != 0):
                passThroughZero += 1

        if dialPosition < 0:
            dialPosition = 100 + dialPosition
            if(not isInitZero):
                passThroughZero += 1


        if dialPosition == 0:
            passThroughZero += 1

        totalZeros += passThroughZero

    return totalZeros

def test_answer():
    rotations = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
    assert countZeros(rotations) == 6

rotations = open('day-1.txt', 'r', encoding="utf-8")
count = countZeros(rotations)
print(count)
rotations.close()

