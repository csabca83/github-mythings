responses={}
flag=True
while flag:
    promt1='Hello,mi a neved? '
    promt2='Melyik hegyre akkarsz menni? '
    promt3='Van meg valaki? '
    name=input(promt1)
    mountain=input(promt2)
    responses[name.lower()]=mountain.lower()
    question_again=input(promt3)
    if question_again.lower()=='nem' or question_again.lower()=='nincs':
        flag=False
        for key,value in responses.items():
            print(key.title(),'a',value.title(),'-ra akkar menni!\n')

