#Parent class for all scheduling algorithms
class algorithm(object):
  def __init__(self,weekSchedule,personSchedule):
    self.weekSchedule = weekSchedule
    self.personSchedule = personSchedule

#Fill by constrained person heuristic
class fill_people(algorithm):
  pass

class fill_days(algorithm):
  pass
