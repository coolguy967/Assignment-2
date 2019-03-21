import random

distances = [[0, 172, 145, 607, 329, 72, 312, 120],
                 [172, 0, 192, 494, 209, 158, 216, 92],
                 [145, 192, 0, 490, 237, 75, 205, 100],
                 [607, 494, 490, 0, 286, 545, 296, 489],
                 [329, 209, 237, 286, 0, 421, 49, 208],
                 [72, 158, 75, 545, 421, 0, 249, 75],
                 [312, 216, 205, 296, 49, 249, 0, 194],
                 [120, 92, 100, 489, 208, 75, 194, 0]]

#The following methid is used to find the total distance travled between all cities.
def getFittest(distances):
    start = random.randint(0, 7)
    sum = 0
    pos = 0
    cur_city = []

    for city in range(len(distances)):

        try:
            cur_city = removeZero(distances[start])
        except ValueError:
            pass

        try:
            pos = cur_city.index(min(cur_city))
            sum += min(cur_city)
        except ValueError:
            pass

        if start < pos:
            pos -= 1

        start = pos

        for i in range(len(distances)):
            try:
                del distances[i][start]
            except IndexError:
                pass

    return sum


def removeZero(city):
    del city[city.index(0)]
    return city


total = 5000 #We set the total distance to a high number so we can compare and find the shortest distance

print("Initial distance: " + str(getFittest(distances)))

#The main loop for finding the shortest distance, runs 10 times to ensure the shortest distance is found in reasonable time.
for i in range(10):

    distances = [[0, 172, 145, 607, 329, 72, 312, 120],
                 [172, 0, 192, 494, 209, 158, 216, 92],
                 [145, 192, 0, 490, 237, 75, 205, 100],
                 [607, 494, 490, 0, 286, 545, 296, 489],
                 [329, 209, 237, 286, 0, 421, 49, 208],
                 [72, 158, 75, 545, 421, 0, 249, 75],
                 [312, 216, 205, 296, 49, 249, 0, 194],
                 [120, 92, 100, 489, 208, 75, 194, 0]]

    cur_total = getFittest(distances)

    if cur_total < total:
        total = cur_total

print("Optimal distance: " + str(total))
