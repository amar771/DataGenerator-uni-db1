'''
Python 3
Generates data about tickets
'''
from random import randint


def write_to_tickets(startID, endID):
    services = [1, 2, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20]

    problems = ['Can\'t ', 'Problem ', 'Doesn\'t work ', 'Broken ', 'Ne radi ',
                'Nece ', 'Problem sa ', 'Nista nece ', 'Stuff ain\'t working ',
                'Popravi ovo sto nece ', 'No idea ', 'Fix ']
    pleases = ['please ', 'pls ', 'plz ', 'molim vas ', 'molim te ',
               'popravi to ', 'de popravi ', 'popravi ovo ',
               'molim te popravi ', 'pls fix ', 'please fix this ',
               'pls fix this ', 'fix this ', 'pleaaase ']
    byes = ['dovidjenja ', 'goodbye ', 'cao ', 'bye ', 'cya ', 'later ',
            'byebye ', 'bye bye ', '...']

    titles = ["Can't buy a service", "Won't buy me a service",
              "Nemogu kupiti", "Nemogu kupiti servis", "Nece da kupi",
              "Nece da kupi servis", "Stuff doesn't work", "Doesn't work",
              "Why doesn't it work?", "Ne radi", "Nece da radi",
              "Zasto ne radi", "Zasto nece da radi", "Broken?",
              "Is it broken", "Why is it broken", "Broken", "Pokvareno",
              "Pokvareno?", "Zasto je pokvareno", "Sto je pokvareno",
              "Fix", "FIX", "Fix!", "FIX!!!", "Popravi", "POPRAVI",
              "Game server broken", "Game server not working",
              "Game server doesn't work", "Igre ne rade",
              "Server za igre ne radi"]

    servers = ["server ", "service ", "game ", "game server ",
               "web ", "web host ", "web hosting ", "game hosting ",
               "serveri ", "servers ", "igre ", "igra "]

    attachment = '"https://www.attach.com/hosting/'
    attachmentTypes = ['.jpg"', '.txt"', '.pdf"', '.gif"', '.doc"', '.docx"',
                       '.ppt"', '.pptx"', '"', '.png"']

    ticketID = 18
    with open("tickets.txt", "w") as file:
        # 3, 1000, 3 - Every third client opens up a ticket
        for i in range(3, 1000, 3):
            service = services[randint(0, len(services)) - 1]

            title = '"'
            title += titles[randint(0, len(titles)) - 1]
            title += '"'

            text = '"'
            text += problems[randint(0, len(problems)) - 1]
            text += servers[randint(0, len(servers)) - 1]
            text += pleases[randint(0, len(pleases)) - 1]
            text += byes[randint(0, len(byes)) - 1]
            text += '"'

            attach = attachment
            attach += str(randint(123456, 987654))
            attach += attachmentTypes[randint(0, len(attachmentTypes)) - 1]

            file.write(str(ticketID) + ',')
            file.write(str(i) + ',')
            file.write(str(service) + ',')
            file.write(title + ',')
            file.write(text + ',')

            # random tickets get attachments
            randNum = randint(0, 3)
            if randNum == 1:
                file.write(attach + ',')
            else:
                file.write(',')

            # random tickets get solved
            randNum = randint(0, 10)
            if randNum == 1:
                file.write('1\n')
            else:
                file.write('0\n')

            ticketID += 1

if __name__ == "__main__":
    startingID = int(input("Enter the starting ID ---> "))
    endingID = int(input("Enter the ending ID ---> "))
    endingID += 1

    write_to_tickets(startingID, endingID)
