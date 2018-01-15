'''
Works with python 3.x
Generates data about client purchases
'''
from random import randint
from datetime import datetime


def get_random_date(lowYear=2016, highYear=2018):
    newDate = datetime(randint(lowYear, highYear),
                       randint(1, 12),
                       randint(1, 28))

    return newDate


def get_dates_sorted(numberOfDatesNeeded):
    dates = []

    for i in range(0, numberOfDatesNeeded):
        newDate = get_random_date()
        dates.append(newDate)

    dates.sort()
    return dates


# Formats dates in Access format:
# m/d/yyyy 0:00:00
def get_date_formatted(date):
    date_string = ''
    date_string += str(date.month) + '/'
    date_string += str(date.day) + '/'
    date_string += str(date.year) + ' '
    date_string += '0:00:00'
    return date_string


def write_to_client_service(startID, endID):
    endID += 1
    services = [1, 2, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20]
    dates = get_dates_sorted(endID-startID)

    dateCounter = 0
    personID = 2
    personCounter = 0
    mandatoryCounter = 0
    with open("clientService.txt", "w") as file:
        for i in range(startID, endID):
            if mandatoryCounter > 40000:
                personID = randint(2, 1000)

            serviceID = services[randint(0, len(services)) - 1]
            date = dates[dateCounter]

            file.write(str(i) + ',')
            file.write(str(personID) + ',')
            file.write(str(serviceID) + ',')
            file.write(get_date_formatted(date))
            file.write('\n')

            dateCounter += 1
            personCounter += 1
            mandatoryCounter += 1

            if personCounter == 4:
                personID += 1
                personCounter = 0


def write_to_client_service_randomized(startID, endID):
    # IDs of services we had in our database
    services = [1, 2, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20]
    dates = get_dates_sorted(endID-startID)

    dateCounter = 0
    with open("clientService.txt", "w") as file:
        for i in range(startID, endID):
            personID = randint(2, 1000)

            serviceID = services[randint(0, len(services)) - 1]
            date = dates[dateCounter]

            file.write(str(i) + ',')
            file.write(str(personID) + ',')
            file.write(str(serviceID) + ',')
            file.write(get_date_formatted(date))
            file.write('\n')

            dateCounter += 1


if __name__ == "__main__":
    startingID = int(input("Enter the starting ID ---> "))
    endingID = int(input("Enter the ending ID ---> "))
    endingID += 1

    write_to_client_service(startingID, endingID)
