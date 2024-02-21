from event import Event

def get_event_date(event):
  return event.date


def current_users(events):
  events.sort(key=get_event_date)
  machines = {}

  for event in events:
    machines[event.machine] = machines.get(event.machine, set())
    if event.type == 'login':
      machines[event.machine].add(event.user)
    elif event.type == 'logout':
      try:
        machines[event.machine].remove(event.user)
      except KeyError:
        print(f"{event.user} was not logged in")

  return machines


def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ', '.join(users)
      print(f"{machine}: {user_list}")
