def getSumInvalidIds(ranges):
    sum = 0
    # split string into array of ranges
    rangesArr = ranges.split(',')

    for idRange in rangesArr:
        # get the limits of each range
        startAndEnd = idRange.split('-')
        start = int(startAndEnd[0])
        end = int(startAndEnd[1]) + 1

        # for idRange between first and last id
        for id in range(start, end):
            idStr = str(id)
            strLength = len(idStr)

            # ignore numbers that can't be split in two
            if(strLength%2==1): continue

            halfMark = int(strLength/2)
            # find each number that is a sequence of digits repeated twice
            isInvalid = idStr[0:halfMark]==idStr[halfMark:]

            if(isInvalid):
                print(id)
                print(isInvalid)
                # add that number to the sum
                sum += id

        print('----')
    return sum

def test_answer():
    ranges ='11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
    assert getSumInvalidIds(ranges) == 1227775554

with open('day-2.txt', 'r', encoding="utf-8") as f:
    ranges = f.readlines()

input = ranges[0]
sum = getSumInvalidIds(input)
print(sum)


