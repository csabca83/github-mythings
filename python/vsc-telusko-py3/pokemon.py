class Pokemon:
  def __init__(self,name,level,health,max_health,type,is_knocked_out):
    self.name=name
    self.level=level
    self.health=health
    self.max_health=max_health
    self.type=type
    self.is_knocked_out=is_knocked_out
  def lose_health(self,damage):
    self.health=self.health-damage
    if self.health<=0:
      self.is_knocked_out=True
      if self.health<0:
        self.health=0
      print(self.name,'is dead,you need to revive it')
    else:
      print(self.name,'Has',self.health,'health')
  def gain_health(self,heal):
    if self.health<self.max_health:
      self.health+=heal
      if self.health>300:
        self.health=300
      print(self.name,'has',self.health)
    else:
      print('your pokemon has full health')
  def revive(self):
    if self.is_knocked_out==True:
      self.health=1
      print('Your pokemon revived succesfully!')
    else:
      print('Your pokemon is a live!')
pikachu=Pokemon('PIkacsu',85,30,300,'electronic',False)
pikachu.lose_health(10)
Pokemon.revive(pikachu)