def getCountFresh(input: list[str]) -> int:
    ranges = []
    for line in input:
        if line.strip() and "-" in line:
            a, b = line.split("-")
            ranges.append(range(int(a), int(b) + 1))

    ranges.sort(key=lambda r: (r.start, r.stop))

    for i, currentRange in enumerate(ranges):
        j = i + 1
        while j < len(ranges):
            r2 = ranges[j]
            if r2.start <= currentRange.stop:
                currentRange = range(
                    currentRange.start, max(currentRange.stop, r2.stop)
                )
                ranges[i] = currentRange
                del ranges[j]
            else:
                break

    p2 = sum([r.stop - r.start for r in ranges])

    return p2


def test_answer():
    ingredients = [
        "3-5",
        "10-14",
        "11-13",
        "16-20",
        "12-18",
        "",
    ]
    assert getCountFresh(ingredients) == 14


with open("day-5.txt", "r", encoding="utf-8") as f:
    ingredients = f.read().splitlines()

all = getCountFresh(ingredients)
print(all)
