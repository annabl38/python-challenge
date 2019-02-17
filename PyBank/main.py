import os
import csv
csvpath=os.path.join("Resources", "budget_data.csv")

total_months=0
profits=[]
changes=[]
oldrow=867884
greatchange=0
lowchange=0

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader=next(csvreader)

    for row in csvreader:
        total_months=total_months+1
        profits.append(float(row[1]))
        change=float(row[1])-oldrow
        changes.append(change)
        if change > greatchange:
            greatchange=change
            greatmonth=row[0]
        if change < lowchange:
            lowchange=change
            lowmonth=row[0]
        oldrow=float(row[1])

averagechange=round(sum(changes)/(len(changes)-1),2)
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {greatmonth} ({greatchange})")
print(f"Greatest Decrease in Profits: {lowmonth} ({lowchange})")

txtfile=open("FinAnalysis.txt", "w")
txtfile.write(f"Financial Analysis\n")
txtfile.write("-------------------\n")
txtfile.write(f"Total Months: {total_months}\n")
txtfile.write(f"Total: ${sum(profits)}\n")
txtfile.write(f"Average Change: ${averagechange}\n")
txtfile.write(f"Greatest Increase in Profits: {greatmonth} ({greatchange})\n")
txtfile.write(f"Greatest Decrease in Profits: {lowmonth} ({lowchange})\n")

  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
