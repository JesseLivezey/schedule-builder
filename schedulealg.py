#Parent class for all scheduling algorithms
class algorithm(object):
  def __init__(self,daysSchedule,peopleSchedule):
    self.daysSchedule = daysSchedule
    self.peopleSchedule = peopleSchedule

  def get_daysSchedule(self):
    return self.daysSchedule

  def get_peopleSchedule(self):
    return self.peopleSchedule

#Fill by constrained person heuristic
class fill_people(algorithm):
  pass

class fill_days(algorithm):
  pass
