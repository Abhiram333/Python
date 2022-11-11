def mean(Data):
    sum = 0
    for x in Data:
        sum += x 
    mean = sum / len(Data)
    return mean


def median(Data):
    Data.sort()
    if len(Data)%2 != 0:
        median = Data[int(len(Data)/2)]
    else:
        median = Data[(int(len(Data)/2)) - 1] +  Data[int(len(Data)/2)]
        median = median/2
    return median

def minimum(Data):
    minimum = Data[0]

    for number in Data:
        if number < minimum:
            minimum = number
    return minimum

def maximum(Data):
    maximum = Data[0]

    for number in Data:
        if number > maximum:
            maximum = number
    return maximum

def range(Data):
    maximum = Data[0]
    minimum = Data[0]

    for number in Data:
        if number > maximum:
            maximum = number

    for number in Data:
        if number < minimum:
            minimum = number
    
    range = maximum - minimum 
    
    return range



def mode(Data):
    moreMode = []
    num = Data[0]
    counter = 0

    for i in Data:
        curr_frequency = Data.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
        elif(curr_frequency == counter and counter > 1):
            if i not in moreMode:
                moreMode.append(i)
                if (Data.count(i) > Data.count(moreMode[-2 if len(moreMode) > 1 else -1])):
                    moreMode = []
                    num = i
            
             
        if len(set(Data)) == len(Data):
            return 'Mode does not exist for this dataset'

    return num if len(moreMode) == 0 else moreMode


numList = []

while(True):
    ask = input('Enter a number and enter "done" to finish dataset: ')

    if ask == 'done':
        break
    numList.append(int(ask))

mean = str(mean(numList))
median = str(median(numList))
mode = str(mode(numList))
range = str(range(numList))
minimum = str(minimum(numList))
maximum = str(maximum(numList))

print('\n' + 'Mean: '+ mean + '\n' + 'Median: ' + median + '\n' + 'Mode: ' + mode +'\n' + 'Range: ' + range +'\n' + 'Minimum: ' + minimum +'\n' + 'Maximum: ' + maximum)