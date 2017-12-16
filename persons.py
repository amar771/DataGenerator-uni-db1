import random 
import string

def NameGenerator(size):
    name = '\"'
    name += (random.choice(string.ascii_uppercase))
    for i in range(size - 1):
        name += (random.choice(string.ascii_lowercase))

    name += '\"'
    return name

def AddressGenerator(size):
    address = '\"'
    address += (random.choice(string.ascii_uppercase))
    for i in range(size - 1):
        address += (random.choice(string.ascii_lowercase))

    address += " "
    address += str(random.randint(1,999))
    address += '\"'
    return address

def PhoneNumberAsText(size):
    phone = '\"'
    for number in range(size):
        phone += (random.choice(string.digits))

    phone += '\"'
    return phone

def Generate(startRange, endRange):
    lines = []
    for i in range(startRange, endRange+1):
        line = ''
        line += str(i)
        line += ','
        line += str(random.randint(1,3173959))
        line += ','
        line += NameGenerator(random.randint(6,12))
        line += ','
        line += NameGenerator(random.randint(8,14))
        line += ','
        line += PhoneNumberAsText(9)
        line += ','
        line += AddressGenerator(random.randint(12,20))
        lines.append(line)

    with open("persons.txt", "w") as file:
        for line in lines:
            file.write(line)
            file.write('\n')

if __name__ == "__main__":
   Generate(1005,1000000)
