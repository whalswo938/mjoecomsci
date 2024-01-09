ftball= [
    {'place': 12, 'match points':45, 'no of matches': 20},
    {'place': 15, 'match points':39, 'no of matches': 20}
]
a= input('enter the name of club:')
if a == 'liverpool':
    b = input('select the option(1:place, 2: match points, 3: no of matches)')
    if b == '1':
        if (ftball[1]['place']%10)==1:
            print(f'{ftball[0]['place']}st place')
        elif (ftball[1]['place']%10)==2:
            print(f'{ftball[0]['place']}nd place')
        else:
             print(f'{ftball[0]['place']}th place')
    elif b == '2':
        print(f'match points:{ftball[0]['match points']}')
    elif b == '3':
        print(f'no of matches:{ftball[0]['no of matches']}')


elif a == 'tottenham':
    c = input('select the option(1:place, 2: match points, 3: no of matches)')
    if c == '1':
        if ftball[1]['place']%10==1:
            print(f'{ftball[1]['place']}st place')
        elif ftball[1]['place']%10==2:
            print(f'{ftball[1]['place']}nd place')
        else:
            print(f'{ftball[1]['place']}th place')
    elif c == '2':
        print(f'match points:{ftball[1]['match points']}')
    elif c == '3':
        print(f'no of matches:{ftball[1]['no of matches']}')
