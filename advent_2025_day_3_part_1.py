def getTotalJoltage(banks):
    total = 0
    for bank in banks:
        # find the maximum pair of digits on each row

        # concatenate them as strings and then turn them into an int
        maxForRow = int(str(bank[0]) + str(bank[1]))

        for index, battery in enumerate(bank):
            currentBattery = battery

            # iterate after the current battery, avoiding itself
            for jindex, secondBattery in enumerate(bank[index + 1 :]):
                combinedBatteryStr = str(currentBattery) + str(secondBattery)

                # update the max
                if int(combinedBatteryStr) > maxForRow:
                    maxForRow = int(combinedBatteryStr)

        print("maxForRow", maxForRow)
        print("---------")
        total += maxForRow

    return total


def test_answer():
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    assert getTotalJoltage(banks) == 357


with open("day-3.txt", "r", encoding="utf-8") as f:
    banks = f.readlines()

totalJoltage = getTotalJoltage(banks)
print(totalJoltage)
