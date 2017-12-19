# Python 2

import string
import random
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

def GetRandomDate(lowYear = 2015, highYear = 2017):
    day = str(random.randint(1, 28))
    day = day.rjust(2, '0')
    month = str(random.randint(1, 12))
    month = month.rjust(2, '0')

    date = str(random.randint(lowYear, highYear))
    date += month
    date += day

    return date

def ClearFile(fileName):
    f = open(fileName, 'w')
    f.write('')
    f.close()

def WriteToFileLogin(loginID, name, surname):
    name = name[1:-1]
    surname = surname[1:-1]

    line = str(loginID) + ','
    line += GetEmail(name, surname) + ','
    line += GetUsername(name, surname) + ','
    line += GetPassword() + ','
    line += 'Yes,'
    line += '#PlaceholderForPriority#'

    f = open("login.txt", "a")

    f.write(line)
    f.write('\n')

    f.close()

def WriteToFileClients(loginID):
    ccn = '"'
    ccn += fake.credit_card_number()
    ccn += '"'

    client = loginID + ','
    client += ccn + ','
    client += GetRandomDate()

    f = open("clients.txt", "a")

    f.write(client)
    f.write('\n')

    f.close()

def WriteToFilePersons(start, end):
    lines = []
    ClearFile('login.txt')
    Clearfile('clients.txt')

    for i in range(start, end):
        name = GetFirstName()
        surname = GetLastName()

        WriteToFileLogin(i, name, surname)
        WriteToFileClients(i)

        line = str(i) + ','
        line += str(random.randint(1,3173959)) + ','
        line += name + ','
        line += surname + ','
        line += GetPhoneNumber(9) + ','
        line += GetAddress()
        lines.append(line)

    f = open("persons.txt", "w")
    
    for line in lines:
        f.write(line)
        f.write('\n')

    f.close()

if __name__ == "__main__":
    startingID = int(input("Enter the starting ID ---> "))
    endingID = int(input("Enter the ending ID ---> "))
    endingID += 1
    WriteToFilePersons(startingID, endingID)  
