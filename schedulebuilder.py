# Schedule Builder
# 2012 Jesse Livezey
import sys

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

if __name__ == '__main__':
  main()
