def getNeighbourCount(rows, row, x, y):
    neighbours = 0
    hasPrevRow = 0 <= y - 1 < len(rows)
    hasNextRow = 0 <= y + 1 < len(rows)
    hasPrevCol = 0 <= x - 1 < len(row)
    hasNextCol = 0 <= x + 1 < len(row)
    if hasPrevRow and rows[y - 1][x] != ".":
        neighbours += 1
    if hasNextRow and rows[y + 1][x] != ".":
        neighbours += 1
    if hasPrevCol and rows[y][x - 1] != ".":
        neighbours += 1
    if hasNextCol and rows[y][x + 1] != ".":
        neighbours += 1
    if hasPrevCol and hasPrevRow and rows[y - 1][x - 1] != ".":
        neighbours += 1
    if hasNextCol and hasPrevRow and rows[y - 1][x + 1] != ".":
        neighbours += 1
    if hasPrevCol and hasNextRow and rows[y + 1][x - 1] != ".":
        neighbours += 1
    if hasNextCol and hasNextRow and rows[y + 1][x + 1] != ".":
        neighbours += 1

    return neighbours


def getCountOfRolls(rows):
    total = 0
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if rows[y][x] != "@":
                continue

            neighbours = getNeighbourCount(rows, row, x, y)

            if neighbours < 4:
                total += 1

    return total


def removeAccessibleRolls(rows):
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if rows[y][x] != "@":
                continue

            neighbours = getNeighbourCount(rows, row, x, y)

            if neighbours < 4:
                # ahh every time you remove one, it skews it, so we need to mark them with x in the mean time instead
                rows[y][x] = "x"

    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if rows[y][x] == "x":
                rows[y][x] = "."
    return rows


def forkRolls(rows):
    newRows = [list(row) for row in rows]

    totalRollsRemoved = 0
    removeNext = getCountOfRolls(newRows)

    while removeNext > 0:
        totalRollsRemoved += removeNext
        newRows = removeAccessibleRolls(newRows)

        removeNext = getCountOfRolls(newRows)
        print(removeNext)

    return totalRollsRemoved


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
    assert forkRolls(rolls) == 43


with open("day-4.txt", "r", encoding="utf-8") as f:
    # gotcha - new lines were also being counted
    rolls = [line.rstrip("\n") for line in f.readlines()]

totalRolls = forkRolls(rolls)
print(totalRolls)
