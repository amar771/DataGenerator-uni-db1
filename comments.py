'''
Python 3
Generates some random comments
'''
from random import randint
from datetime import datetime


def get_random_date(lowYear=2016, highYear=2018):
    newDate = datetime(randint(lowYear, highYear),
                       randint(1, 12),
                       randint(1, 28))

    return newDate


def get_sorted_dates(start, end):
    dates = []
    for i in range(start, end):
        newDate = get_random_date()
        dates.append(newDate)

    dates.sort()
    return dates


# Formats the date in Access readable way
# m/d/yyyy 0:00:00
def get_date_formatted(dateToBeFormatted):
    dateString = ''
    dateString += str(dateToBeFormatted.month) + '/'
    dateString += str(dateToBeFormatted.day) + '/'
    dateString += str(dateToBeFormatted.year) + ' '
    dateString += '0:00:00'
    return dateString


# Generates some random comments in a funny way
def write_to_comments(ticketID, commentID):
    contents = ['bump', 'Bump', 'bump...', 'same issue here', 'isti problem',
                'same problem', 'doesn\'t work here either', 'ne radi isto',
                'can be fixed like this', 'moze se ovako popraviti',
                'can\'t be fixed currently', 'trenutno nema fixa',
                'trenutno se ne moze popraviti', 'fix pls', 'fiiiiix',
                'this is annoying', 'uzasno', 'horrible', 'terrible',
                'if you don\'t fix I\'m leaving you', 'fix pleasee',
                'why isn\'t this fixed yet?', 'why isn\'t this fixed',
                'this is serious', 'this is serious problem', 'fix pls',
                'fix plz', 'popravite ovo', 'ovo treba popraviti pod hitno',
                'de popravi ovo', 'de popravite ovo', 'dosta mi je',
                'ovo je  ozbiljan problem', 'ovo ne moze ovako vise',
                'this can\'t go on like this', 'this can\'t go on',
                'this can\'t go on like this any more',
                'this can\'t go on like this any longer']

    check = 0
    good = True
    personID = 3
    # Generates 3 comments per ticket
    with open("comments.txt", "w") as file:
        while good:
            if check == 0:
                dates = get_sorted_dates(1, 4)

            content = '"'
            content += contents[randint(0, len(contents)) - 1]
            content += '"'

            file.write(str(commentID) + ',')
            file.write(str(ticketID) + ',')
            file.write(str(personID) + ',')
            file.write(get_date_formatted(dates[check]) + ',')
            file.write(content + '\n')

            commentID += 1

            # Moves on to the next ticket and next person
            if check == 2:
                check = 0
                ticketID += 1
                personID += 3

                # Stops the execution because it reached the last person
                if personID > 999:
                    good = False

                continue

            check += 1


if __name__ == "__main__":
    starting_ticket_id = int(input("Enter the starting ticket ID ---> "))
    starting_comment_id = int(input("Enter the starting comment ID ---> "))

    write_to_comments(starting_ticket_id, starting_comment_id)
