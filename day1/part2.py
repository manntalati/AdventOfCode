file = open("list.txt", "r") #open the input file as txt file and read it

elves = [] #create an elves array list to store the input
total = 0 #create the total for each specific elf

for line in file:
  if line == "\n": #if line in the input is a new line then end the total calories for the elf and append
    elves.append(total)
    total = 0 #set the total back to 0 so it can be repeated
  else:
    total += int(line) #add calories to total until the newline is encountered

max1 = 0
max2 = 0
max3 = 0
for e in elves: #go through the array to find biggest value and set that equal to max1
  if e > max1:
    max1 = e
elves.remove(max1) #once max1 is found remove from list and repeat process for max2 and max3

for e in elves:
  if e > max2:
    max2 = e
elves.remove(max2)

for e in elves:
  if e > max3:
    max3 = e
    
esum = 0
esum = max1 + max2 + max3 #add all three elf maxes together to figure out what is needed for the top 3 elves' calories
