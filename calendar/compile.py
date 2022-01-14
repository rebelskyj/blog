import subprocess
months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
with open("calendar/calendar.md") as base:
  content = base.read()

with open("calendar/order.txt") as order:
  tmp = ""
  for line in order:
    line = line.strip()
    if line[0] == "*":
      year = int(line[1:])
      content += tmp
      tmp = ""
      content += "<h2>%d</h2>\n" % year
    elif line[0] == "-":
      month = months[line[1:]]
      content += tmp
      tmp = subprocess.check_output(["calendar/mkcal.sh", str(month), str(year)]).decode()
    else:
      title, url, day = line.split(":")
      day = int(day)
      tmp = tmp.replace("<td>%d</td>" % day, "<td><a href='%s'>%s<div>%s</div></a></td>" % (url, str(day), title))

content += tmp

print(content)
