# dial: 0:99
# LX - left x clicks
# RX - right x clicks
# in a circle
# Dial start = 50

# count times when dial = 0 after each rotation

def countZeros(rotations):
    dialPosition = 50
    countOfZeros = 0
    for rotation in rotations:
        direction = rotation[0]
        clicks = rotation[1:]
        clicks = int(clicks)

        print('dialPosition', dialPosition)
        print('rotation',rotation)
        print('clicks',clicks)
        clicks = clicks%100
        print('normalised Clicks', clicks)

        if direction == 'L':
            dialPosition -= clicks
        if direction == 'R':
            dialPosition += clicks

        if dialPosition > 99:
            dialPosition -= 100
        if dialPosition < 0:
            dialPosition = 100 + dialPosition

        if dialPosition == 0:
            countOfZeros += 1

        print('new dialPosition',dialPosition)
        print('-----')
    return countOfZeros


def test_answer():
    rotations = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
    assert countZeros(rotations) == 3

rotations = open('day-1.txt', 'r', encoding="utf-8")
count = countZeros(rotations)
print(count)
rotations.close()

