import time

i = 0
while i <= 3600:
  f = open("task2.out.txt", "a")
  time.sleep(1)
  f.write(str(i))
  f.write("\n")
  f.close()
  i += 1

#open and read the file after the appending:
#f = open("task2.out.txt", "r")
#print(f.read())
#f.close()

