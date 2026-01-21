def getCountFresh(ingredients: list[str]) -> int:
    countFresh = 0

    idxOfBreak = ingredients.index("")
    ranges = ingredients[0:idxOfBreak]
    products = ingredients[idxOfBreak + 1 :]
    for product in products:
        for range in ranges:
            startAndEndOfRange = range.split("-")
            start = int(startAndEndOfRange[0])
            end = int(startAndEndOfRange[1]) + 1
            if start <= int(product) <= end:
                countFresh += 1
                break

    return countFresh


def test_answer():
    ingredients = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]
    assert getCountFresh(ingredients) == 3


with open("day-5.txt", "r", encoding="utf-8") as f:
    ingredients = f.read().splitlines()

all = getCountFresh(ingredients)
print(all)
