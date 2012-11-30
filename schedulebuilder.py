# Schedule Builder
# 2012 Jesse Livezey
import sys
import schedulealg

def read_human_schedule(filename):
  f = open(filename,'r')
  scheduleDict = {}
  for line in f:
    tempLine = line.split()
    sections = tempLine[2:]
    sections.append(len(sections))
    scheduleDict[tempLine[0]+' '+tempLine[1]] = sections
  f.close()
  return scheduleDict

def read_day_schedule(filename):
  f = open(filename,'r')
  scheduleDict = {}
  for line in f:
    tempLine = line.split()
    scheduleDict[tempLine[0]] = tempLine[1:]
  f.close()
  return scheduleDict


def main():

  human = sys.argv[1]
  day = sys.argv[2]
  people = read_human_schedule(human)
  days = read_day_schedule(day)
  schedule1 = schedulealg.fill_people()
  schedule1.set_peopleSchedule(people)
  schedule1.set_daysSchedule(days)
  schedule2 = schedulealg.fill_days()
  schedule2.set_peopleSchedule(people)
  schedule2.set_daysSchedule(days)
  schedule2.make_schedule()
  print schedule1.get_peopleSchedule()
  print schedule2.get_daysSchedule()

if __name__ == '__main__':
  main()
