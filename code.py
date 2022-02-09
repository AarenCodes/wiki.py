import datetime

answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://wikipedia.org/wiki/{}'

while True:
    answer = input("What date would you like? Enter MM/DD. Enter quit to quit ")
    if answer.upper() == 'QUIT':
        break
        
        
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
        
    except ValueError:
        print("That is not a valid date, please try again.")
