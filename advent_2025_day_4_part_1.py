def getRollCount(rows):
    total = 0
    for y, row in enumerate(rows):
        print(rows[y])
        for x, col in enumerate(row):
            if rows[y][x] != "@":
                continue

            neighbours = 0
            hasPrevRow = 0 <= y - 1 < len(rows)
            hasNextRow = 0 <= y + 1 < len(rows)
            hasPrevCol = 0 <= x - 1 < len(row)
            hasNextCol = 0 <= x + 1 < len(row)
            if hasPrevRow and rows[y - 1][x] == "@":
                neighbours += 1
            if hasNextRow and rows[y + 1][x] == "@":
                neighbours += 1
            if hasPrevCol and rows[y][x - 1] == "@":
                neighbours += 1
            if hasNextCol and rows[y][x + 1] == "@":
                neighbours += 1
            if hasPrevCol and hasPrevRow and rows[y - 1][x - 1] == "@":
                neighbours += 1
            if hasNextCol and hasPrevRow and rows[y - 1][x + 1] == "@":
                neighbours += 1
            if hasPrevCol and hasNextRow and rows[y + 1][x - 1] == "@":
                neighbours += 1
            if hasNextCol and hasNextRow and rows[y + 1][x + 1] == "@":
                neighbours += 1

            if neighbours < 4:
                total += 1

    print(total)

    return total


def test_answer():
    rolls = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    assert getRollCount(rolls) == 13


with open("day-4.txt", "r", encoding="utf-8") as f:
    rolls = f.readlines()

totalRolls = getRollCount(rolls)
print(totalRolls)
