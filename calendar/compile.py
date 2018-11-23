with open("calendar/calendar.md") as base:
  content = base.read().split("\n")

with open("calendar/order.txt") as order:
  for line in order:
    title, url, date = line.split(":")
    month, day = date.strip().split(" ")
    result = []
    found = False
    done = False
    for line in content:
      if(not done):
        if(not found):
          if(line.find(month) != -1):
            found = True
        else:
          try:
            if(int(line.split(">")[1].split("<")[0]) == int(day)):
              line = "      <td><a href='%s'>%s<div>%s</div></a></td>" % (url, str(int(day)), title)
              done = True
          except:
            pass
      result.append(line)
    content = result

print("\n".join(content))
