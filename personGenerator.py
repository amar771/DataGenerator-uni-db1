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

def WriteToFile(start, end):
    lines = []
    line = ''
    for i in range(start, end):
        line = ''
        line += str(i)
        line += ','
        line += str(random.randint(1,3173959))
        line += ','
        line += GetFirstName()
        line += ','
        line += GetLastName()
        line += ','
        line += GetPhoneNumber(9)
        line += ','
        line += GetAddress()
        lines.append(line)

    f = open("persons.txt", "w")
    
    for line in lines:
        f.write(line)
        f.write('\n')

    f.close()

if __name__ == "__main__":
    WriteToFile(1, 11)
    #GetAddress()
