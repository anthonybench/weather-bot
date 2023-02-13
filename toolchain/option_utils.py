from typing import List, Union

'''
help(usageMessage)
help(verifyOption)
help(checkListOverlap)
help(getOptionVal)
help(stripOptionVals)
'''

def usageMessage(errorNotice: str = '') -> str:
  '''Takes optional error message.
Prints usage message'''
  if errorNotice:
    errorNotice += '\n\n'
  print(f"""
{errorNotice}
Simply run main.py to log the bot in indefinitely.
--------------
Usage:
  ./main.py
Info:
  ./main.py [-h|--help]
--------------
""")


def verifyOption(args: List[str], options: dict) -> bool:
  '''Takes list of user arg strings and options dictionary.
Returns True if option flag exists and value matches required type, else False.'''
  res = []
  for arg in args:
    flag = False
    if '=' in arg:
      pretext = arg[:arg.index('=')+1]
      val = arg[arg.index('=')+1:]
      for optionTypeName in options:
        if options[optionTypeName][0] == pretext:
          if (options[optionTypeName][1] == 'int') and (val.isdigit()):
            flag = True
          elif (options[optionTypeName][1] == 'str') and (not val.isdigit()):
            flag = True
    else:
      for optionTypeName in options:
        for opFlag in options[optionTypeName]:
          if arg == opFlag:
            flag = True
    res.append(flag)
  return (False not in res)


def checkListOverlap(l1: List[str], l2: List[str]) -> bool:
  '''Takes 2 lists of strings.
Returns True if lists share elements, else False.'''
  return [i for i in l1 if i in l2] != []


def getOptionVal(args: List[str], key: List[str]) -> Union[str,int]:
  '''Takes list of user arg strings and list of option strings ([--myop=val,type]).
Returns val in it's intended type'''
  for arg in args:
    if key[0] in arg:
      val = arg[arg.index('=')+1:]
      if key[1].lower() == 'int':
        return int(val)
      elif key[1].lower() == 'str':
        return val
      else:
        return val


def stripOptionVals(args: List[str]) -> List[str]:
  '''Takes list of user arg strings.
Returns filtered list of all user args containing values, with said values stripped (equals sign is preserved).'''
  res = []
  for arg in args:
    if '=' in arg:
      res.append(arg[:arg.index('=')+1])
    else:
      res.append(arg)
  return res
