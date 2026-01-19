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
            print('idStr', idStr)
            # find each number that is a sequence of digits repeated at least twice
            isInvalid = False
            # all digits are the same
            # two sides are mirrorred

            # for each character in string
            # if current unmber is the same as all numbers in the string
            # if substring so far appears n times, equal to string length *n times= total string length

            for index,digit in enumerate(idStr):
                chunkLength = index+1

                # the id should be entirely composed of duplicates
                if(strLength%chunkLength!= 0):
                    continue

                # ignore the last iteration because it's selfsame
                if(chunkLength==strLength):
                    continue

                chunksCount = int(strLength / chunkLength)
                currentChunk = idStr[0:chunkLength]
                print('chunksCount',chunksCount)
                print('currentChunk',currentChunk)
                print('currentChunk*chunksCount',currentChunk*chunksCount)

                # does it consist of repeats?
                if(currentChunk*chunksCount == idStr):
                    isInvalid = True
                    break


            if(isInvalid):
                print('add it')
                sum += id
            else:
                print('ignore')
            print('  ')

        print('----')
    return sum

def test_answer():
    ranges ='11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
    assert getSumInvalidIds(ranges) == 4174379265



with open('day-2.txt', 'r', encoding="utf-8") as f:
    ranges = f.readlines()

input = ranges[0]
sum = getSumInvalidIds(input)
print(sum)


