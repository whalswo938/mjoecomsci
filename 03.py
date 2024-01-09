ftball= [
    {'place': 12, 'match points':45, 'no of matches': 20},
    {'place': 15, 'match points':39, 'no of matches': 20}
]

iptno = int(input('enter the number you want to delete:'))
for ft in ftball:
    if ft['place']==iptno:
        ftball.remove(ft)
        print(ft)