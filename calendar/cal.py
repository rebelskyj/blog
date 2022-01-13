from sys import argv
cal = argv[1].replace("_\x08", "") # Remove Mac cal highlight
cal = cal.split("\n")
with open("calendar/month.md") as file:
  month_temp = file.read()

month = cal[0].strip().split(" ")[0]
cal = filter(lambda x: len(x.strip()) > 0, cal[2:])
cal = map(lambda row: [row[i*3: i*3 + 2].strip() for i in range(7)], cal)
cal = map(lambda row: "    <tr>\n%s\n    </tr>" % "\n".join(
  list(
    map(
      lambda cell: "      <td>%s</td>" % cell, row
    )
  )
), cal)

print(month_temp.replace("{month}", month).replace("{body}", "\n".join(cal)))
