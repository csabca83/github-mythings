unconfirmed_users=['lali','nemtom','bela']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print('ezeknek meg varniuk kell',current_user)
    
for user in confirmed_users:
    print('lehet orulni ti bejutotatok',user,)
