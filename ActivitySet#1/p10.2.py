# Tuples

'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

filename = "mbox-short.txt"
lst = list()
d = dict()
if len(filename) < 1:
    filename = "mbox-short.txt"
handle = open(filename)
for line in handle:
    if line.startswith("From:"):
         continue
    if line.startswith("From"):
       spt = line.split()
       ele = spt[5]
       lst.append(ele[:2])
       lst.sort()
for key in lst:
  if key not in d:
    d[key] = 1
  else:
    d[key] += 1
for k,v in d.items():
  print(k,v)