"""
   Python 2.7.14
   Random data generator using faker library.
"""

import string
import random

from datetime import datetime
from string import split
from faker import Faker

fake = Faker()


def GetFirstName():
    nameList = split(fake.name())
    while len(nameList) > 2:
        nameList = split(fake.name())

    name = '\"'
    name += str(nameList[0])
    name += '\"'
    return name


def GetLastName():
    nameList = split(fake.name())
    while len(nameList) > 2:
        nameList = split(fake.name())

    lastName = '\"'
    lastName += str(nameList[1])
    lastName += '\"'
    return lastName


def GetAddress():
    address = fake.address()
    while len(address) > 35:
        address = str(fake.address())

    addressList = split(address)
    finalAddress = '\"'
    for i in addressList:
        finalAddress += str(i)
        finalAddress += ' '

    finalAddress += '\"'
    return finalAddress


def GetPhoneNumber(size):
    phone = '\"'
    for i in range(size):
        phone += (random.choice(string.digits))

    phone += '\"'
    return phone


def GetEmail(name, surname):
    providers = ['gmail.com', 'yahoo.com', 'hotmail.com',
                 'outlook.com', 'edu.fit.ba', 'mail.com',
                 'protonmail.com', 'aol.com', 'yandex.com', 'zoho.com']

    email = '"' + name + surname + '@' + \
            providers[random.randint(0, len(providers)) - 1] + \
            '"'

    return email


def GetPassword():
    password = '"'
    password += 'password'
    for i in range(8):
        password += random.choice(string.digits)

    password += '"'
    return password


def GetUsername(name, surname):
    username = '"' + name + surname
    for i in range(3):
        username += random.choice(string.digits)

    username += '"'
    return username


def GetRandomDate(lowYear=2015, highYear=2017):
    newDate = datetime(random.randint(lowYear, highYear),
                       random.randint(1, 12),
                       random.randint(1, 28))

    return newDate


def GetAllDatesSorted(start, end):
    dates = []
    for i in range(start, end):
        newDate = GetRandomDate()
        dates.append(newDate)

    dates.sort()
    return dates


def GetDateFormatted(dateToBeFormatted):
    dateString = ''
    dateString += str(dateToBeFormatted.month) + '/'
    dateString += str(dateToBeFormatted.day) + '/'
    dateString += str(dateToBeFormatted.year) + ' '
    dateString += '0:00:00'
    return dateString


def ClearFile(fileName):
    """
     Cleans all files from previously generated data
     becuase data in files is connected
    """
    f = open(fileName, 'w')
    f.write('')
    f.close()


def WriteToFileLogin(loginID, name, surname):
    """
     Writes data to login.txt
     Format:
     id,permission[0-none],email,username,password,active[1-true]
    """
    name = name[1:-1]
    surname = surname[1:-1]

    line = str(loginID) + ','
    line += '0'
    line += GetEmail(name, surname) + ','
    line += GetUsername(name, surname) + ','
    line += GetPassword() + ','
    line += '1'

    f = open("login.txt", "a")

    f.write(line)
    f.write('\n')

    f.close()


def WriteToFileClients(loginID, registrationDate):
    """
     Writes data to clients.txt
     Format:
     id,creditcard,registrationdate[MM\DD\YYYY H:MM:SS]
    """
    ccn = '"'
    ccn += fake.credit_card_number()
    ccn += '"'

    client = str(loginID) + ','
    client += ccn + ','
    client += GetDateFormatted(registrationDate)

    f = open("clients.txt", "a")

    f.write(client)
    f.write('\n')

    f.close()


def WriteToFilePersons(start, end):
    """
     Writes to file persons.txt
     This is the main one, for every line of data it adds it adds
     corresponding data to login.txt and clients.txt by calling
     appropriate functions.
     Format:
     id,cityID,name,surname,phone,address
    """
    ClearFile('login.txt')
    ClearFile('clients.txt')

    listOfDates = GetAllDatesSorted(start, end)
    listOfDatesCounter = int(0)

    f = open("persons.txt", "w")

    for i in range(start, end):
        name = GetFirstName()
        surname = GetLastName()

        WriteToFileLogin(i, name, surname)
        WriteToFileClients(i, listOfDates[listOfDatesCounter])
        listOfDatesCounter += 1

        line = str(i) + ','
        line += str(random.randint(1, 3173959)) + ','
        line += name + ','
        line += surname + ','
        line += GetPhoneNumber(9) + ','
        line += GetAddress()
        f.write(line)
        f.write('\n')

    f.close()


if __name__ == "__main__":
    """
     Asks user for starting ID (in case some data is already entered
     and ending ID
     number of rows/lines = endingID - startingID
    """
    startingID = int(input("Enter the starting ID ---> "))
    endingID = int(input("Enter the ending ID ---> "))
    endingID += 1

    WriteToFilePersons(startingID, endingID)
