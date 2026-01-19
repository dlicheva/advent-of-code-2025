# I am stuck here - giving up after 3h
def getTotalJoltage(banks):
    total = 0
    for bank in banks:
        # find the maximum 12 ordered digits on each row
        maxJolt = ""
        # start = 0
        # batteries = 12
        # for remaining in range(batteries, 0, -1):
        #     # find the highest digit in the range, where there is enough space for the remaining batteries
        #     end = len(bank) - (remaining - 1)
        #     first_digit = max(bank[start:end])
        #
        #     # add to the result
        #     maxJolt += first_digit
        #
        #     # next iteration will start from the battery after this one
        #     start = bank.index(first_digit, start) + 1
        print("new bank", maxJolt)
        print("---------")

    return total


def test_answer():
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    assert getTotalJoltage(banks) == 3121910778619


with open("day-3.txt", "r", encoding="utf-8") as f:
    banks = f.readlines()

totalJoltage = getTotalJoltage(banks)
print(totalJoltage)
