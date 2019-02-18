import os
import csv
csvpath=os.path.join("Resources", "election_data.csv")

totalvotes=0
votecounts={}

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader=next(csvreader)

    for row in csvreader:
        totalvotes=totalvotes+1
        if row[2] not in votecounts:
            votecounts[row[2]]=1
        else:
            votecounts[row[2]]=votecounts[row[2]]+1
#Election Results
 # -------------------------
 # Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
 # Correy: 20.000% (704200)
 #Li: 14.000% (492940)
 # O'Tooley: 3.000% (105630)
  #-------------------------
 # Winner: Khan
 # -------------------------

txtfile=open("electionresults.txt","w")
print(f"Election Results")
txtfile.write(f"Election Results\n")
print("-----------")
txtfile.write("-----------\n")
print(f"Total Votes: {totalvotes}")
txtfile.write(f"Total Votes: {totalvotes}\n")
print("------------")
txtfile.write("------------\n")
winnervote=0
for name in votecounts:
    count=votecounts[name]
    percentvote=count/totalvotes
    if count > winnervote:
        winnervote=count
        winner=name
    print(f"{name}: {percentvote:.2%} ({count})")
    txtfile.write(f"{name}: {percentvote:.2%} ({count})\n")
print("----------")
txtfile.write("----------\n")
print(f"Winner: {winner}")
txtfile.write(f"Winner: {winner}\n")



