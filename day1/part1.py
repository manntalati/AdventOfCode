file = open("list.txt", "r") #open the input file as txt file and read it


elves = [] #create an elves array list to store the input
total = 0 #create the total for each specific elf
for line in file: 
  if line == "\n": #if line in the input is a new line then end the total calories for the elf and append
    elves.append(total)
    total = 0 #set the total back to 0 so it can be repeated
  else:
    total += int(line) #add calories to total until the newline is encountered

max = 0 
for e in elves: #go through each entry in the array to find max
  if e > max: #once the entry is bigger than max replace it and max will be the largest number of calories for an elf
    max = e
