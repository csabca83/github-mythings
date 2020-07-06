def print_out(arg):
  print(arg)
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005
vehicle=VehicleInsurance(5)
home=HomeInsurance(4)
for x in [vehicle,home]:
  print_out(x.get_rate())
