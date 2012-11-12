# Schedule Builder
# 2012 Jesse Livezey
import sys
import schedulealg

def read_human_schedule(filename):
  f = open(filename,'r')
  scheduleDict = {}
  for line in f:
    tempLine = line.split()
    scheduleDict[tempLine[0]+' '+tempLine[1]] = tempLine[2:]
  f.close()
  print(scheduleDict)

def read_day_schedule(filename):
  f = open(filename,'r')
  scheduleDict = {}
  for line in f:
    tempLine = line.split()
    scheduleDict[tempLine[0]] = tempLine[1:]
  f.close()
  print(scheduleDict)



def main():

  human = sys.argv[1]
  day = sys.argv[2]
  read_human_schedule(human)
  read_day_schedule(day)
  schedule1 = schedulealg.fill_people(human,day)
  schedule2 = schedulealg.fill_days(human,day)
  print(schedule1.get_peopleSchedule())
  print(schedule2.get_daysSchedule())

if __name__ == '__main__':
  main()
