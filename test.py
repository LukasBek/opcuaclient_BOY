import ast

f = open('BOY_DATA_2021-12-17-14-35-37.txt', 'r')
readings = f.readlines()
sortedReadings = []

for reading in readings:
    sortedReadings.append(reading.split(','))


def convert(val):
    constructors = [int, float, str]
    for c in constructors:
        try:
            return c(val)
        except ValueError:
            pass


def convert_list():
    for i in range(len(sortedReadings)):
        newlist = [convert(x) for x in sortedReadings[i]]
        sortedReadings[i] = newlist



if __name__ == '__main__':
    convert_list()
    print(sortedReadings[112])

        # print(i)
        #print(sortedReadings[i][i])
        #print(sortedReadings[0][i])
        #print(tryeval(sortedReadings[0][i]))
        #print(type(tryeval(sortedReadings[0][i])))


