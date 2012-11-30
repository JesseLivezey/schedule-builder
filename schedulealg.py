import operator
#Parent class for all scheduling algorithms
class algorithm(object):
  def __init__(self):
    pass
    
  def set_peopleSchedule(self,schedule):
    self.peopleSchedule = schedule

  def set_daysSchedule(self,schedule):
    self.daysSchedule = schedule

  def get_daysSchedule(self):
    return self.daysSchedule

  def get_peopleSchedule(self):
    return self.peopleSchedule

#Fill by constrained person heuristic
class fill_people(algorithm):
  def make_schedule(self):
    pass  
class fill_days(algorithm):
  def make_schedule(self):
    sortedDays = sorted(self.daysSchedule.iteritems(),key=operator.itemgetter(1),reverse=True)
    print sortedDays
    #sortedPeople = sorted(self.peopleSchedule.iteritems(),key = len(operator.itemgetter(1)),reverse = True)
    #print 
    #print sortedPeople
