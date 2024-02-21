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


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)