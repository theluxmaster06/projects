model_choice = input("Enter the model of the car: ")

thisdict = {
  "brand": "Ford",
  "model": "",
  "year": 1964,
  "color": ""
}

for x in thisdict:
  if thisdict[x]:
    print(f"{x} is {thisdict[x]}")

thisdict["model"] = model_choice

for x in thisdict:
  if thisdict[x]:
    print(f"{x} is {thisdict[x]}")


