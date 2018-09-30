with open("sources/order.txt") as order:
  content = order.read()

if(content[-1] != "\n"):
  with open("sources/order.txt", "w") as order:
    order.write(content)
    order.write("\n")
