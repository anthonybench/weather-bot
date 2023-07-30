# stdlib
from typing import List
from sys import exit
# 3rd party
try:
  pass
except ModuleNotFoundError as e:
  print("Error: Missing one or more 3rd-party packages (pip install).")
  exit(1)


#───Utils────────────────────
def sort_days(days: List[str], today: str) -> List[str]:
  '''takes list of day-names and current day, returns days in order given current day'''
  
  next_day = {'Monday':'Tuesday','Tuesday':'Wednesday','Wednesday':'Thursday','Thursday':'Friday','Friday':'Saturday','Saturday':'Sunday','Sunday':'Monday'}
  payload = []
  ptr     = next_day[today]
  for i in range(len(days)):
    payload.append(ptr)
    ptr = next_day[ptr]
  return payload