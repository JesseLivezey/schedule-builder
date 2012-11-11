# Schedule Builder
# 2012 Jesse Livezey
import sys

def read_human_schedule(filename):
  f = open(filename,'r')
  names = f.read()
  scheduleDict = {}
  for line in f:
    tempLine = line.split()
    scheduleDict[tempLine[0]] = tempLine[1:]

def read_day_schedule(filename):
  f = open(filename,'r')
  days = f.read()
  scheduleDict = {}
  for line in f:
    tempLine = line.split()
    scheduleDict[tempLine[0]] = tempLine[1:]



def main():

  human = sys.argv[1]
  day = sys.argv[2]
  read_human_schedul(human)
  iread_day_schedule(day)
if __name__ == '__main__':
  main()
