def prod(factors):
    p = 1
    for i in factors:
        p *= i
    return p


def rotate_90_degrees(matrix):
    rotated_matrix = []
    for i, horNumber in enumerate(matrix[0]):
        newRow = []
        for j, vertNumber in enumerate(matrix):
            newRow.insert(0, matrix[j][i])
        rotated_matrix.append(newRow)

    return rotated_matrix


def getGrandTotal(rows: list[str]) -> int:
    total = 0
    arrayed = []
    for val in rows:
        arrayOfVals = val.split()
        arrayed.append(arrayOfVals)

    arrayed = rotate_90_degrees(arrayed)

    for row in arrayed:
        factors = [int(x) for x in row[1:]]
        print(row)
        if row[0] == "+":
            total += sum(factors)
        elif row[0] == "*":
            total += prod(factors)

    return total


def test_answer():
    problems = [
        "123 328  51 64",
        "45 64  387 23",
        "6 98  215 314",
        "*   +   *   +  ",
    ]
    assert getGrandTotal(problems) == 4277556


with open("day-6.txt", "r", encoding="utf-8") as f:
    problems = f.read().splitlines()

all = getGrandTotal(problems)
print(all)
