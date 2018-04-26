from random import randint
import time
from matplotlib import pyplot as plt

#standard insertion sort
def insertionSort(testList):
    if(not testList):
        return testList

    for i in range(1,len(testList)):

        currentVal = testList[i]
        currentI = i

        while currentI > 0 and testList[currentI-1] > currentVal:
            testList[currentI] = testList[currentI-1]
            currentI -= 1

        testList[currentI] = currentVal
     
    return testList

#bucket sort that uses insertion sort on buckets
def bucketSort1(testList, bucketDenom, plot):
    buckets = []

    #allocate a number of buckets determined by bucketDenom
    for i in range(max(testList)/bucketDenom + 1):
        buckets.append([])

    #put values into the buckets
    for val in testList:
        buckets[val/bucketDenom].append(val)

    #plot the data if needed
    if(plot):
        plt.figure(3)
        y = []
        for bucket in buckets:
            for val in bucket:
                y.append(val)

        plt.bar(range(len(testList)), y, color = 'white')
        plt.title('Bucketed, Unsorted Data')

    #sort each bucket
    for index, bucket in enumerate(buckets):
        buckets[index] = insertionSort(bucket)

    #stitch together sorted buckets
    newList = []
    for bucket in buckets:
        for val in bucket:
            newList.append(val)

    return newList

def bucketSort2(testList, bucketDenom):
    buckets = []

    #allocate a number of buckets determined by bucketDenom
    for i in range(max(testList)/bucketDenom + 1):
        buckets.append([])

    #put values into the buckets
    for val in testList:
        buckets[val/bucketDenom].append(val)

    #stitch the buckets back together
    newList = []
    for bucket in buckets:
        for val in bucket:
            newList.append(val)

    #sort the stitched buckets
    insertionSort(newList)

    return newList

listSize = 1000
test1 = [0]*listSize
test2 = [0]*listSize

x = []
y1 = []
y2 = []

#generate lists of 1000 random ints, and sort them with bucketsorts with a varied number of buckets (1 - 10,000)
for i in range(17):
    for j in range(listSize):
        test1[j] = randint(0, 10000)
        test2[j] = randint(0, 10000)

    bucketDenom = int(round(pow(10, i/4.0)))
    anchor = time.clock()
    bucketSort1(test1, bucketDenom, False)
    y1.append(time.clock() - anchor)
    anchor = time.clock()
    bucketSort2(test2, bucketDenom)
    y2.append(time.clock() - anchor)
    x.append(100000.0/bucketDenom)

plt.rcParams['axes.facecolor'] = '#242128'
plt.rcParams['figure.facecolor'] = '#242128'
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['text.color'] = 'white'
plt.figure(1)
plot1, = plt.plot(x, y1, 'w')
plt.xlabel('# of buckets')
plt.ylabel('sort time (s)')
plot2, = plt.plot(x, y2, 'c')
plt.legend([plot1, plot2], ['sort before stitch', 'sort after stitch'])
plt.title('Time to sort 1000 elements')
plt.xscale('log')
for j in range(listSize):
    test1[j] = randint(0, 10000)
plt.figure(2)
plt.bar(range(listSize), test1, color = 'white')
plt.title('Raw Data')
bucketSort1(test1, 1000, True)
plt.show()








