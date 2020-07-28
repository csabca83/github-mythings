class Dunderek:
    def __init__(self,obj1):
        self.obj1=obj1
    def __add__(self,other):
        return self.obj1+other.obj1
fi=Dunderek(15)
se=Dunderek(39)
th=fi+se
class Iter:
    def __init__(self,lst):
        self.lst=lst
    def __iter__(self):
        return iter(self.lst)
i=Iter(['na','szosz','van'])
for x in i:
    print(x)

class UserGroup:
  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions

  def __iter__(self):
    return iter(self.user_list)

  def __len__(self):
    return len(self.user_list)

  def __contains__(self, user):
    return user in self.user_list