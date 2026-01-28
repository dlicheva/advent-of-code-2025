def getGrandTotal(rows: list[str]) -> int:
    a = 0
    # split each row into an array of numbers
    # save all the arrays
    arrayed = []
    for val in rows:
        arrayOfVals = val.split()
        arrayed.append(arrayOfVals)

    print(arrayed)

    for i, number in enumerate(arrayed[0]):
        operation = arrayed[-1][i]
        totalForCol = 0
        if(operation == '+'):
            for param in arrayed:


    # for each item in the first row
    # find the operation
    # find all other params
    # get the result
    # add it to the total

    return a


def test_answer():
    problems = [
        "123 328  51 64",
        "45 64  387 23",
        "6 98  215 314",
        "*   +   *   +  ",
    ]
    assert getGrandTotal(problems) == 4277556


problems = [
    "123 328  51 64",
    "45 64  387 23",
    "6 98  215 314",
    "*   +   *   +  ",
]
getGrandTotal(problems)
#
# with open("day-6.txt", "r", encoding="utf-8") as f:
#     problems = f.read().splitlines()
#
# all = getGrandTotal(problems)
# print(all)
