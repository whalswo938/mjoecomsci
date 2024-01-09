num=[1,3,5,7,9]
isfind=False
for i in num:
    if i==num:
        print(True)
        isfind=True
if isfind==False:
    print(False)