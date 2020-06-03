import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

  PyBank = csv.reader(csvfile, delimiter=',')

  csv_header = next(PyBank)

  with open("file.txt", "w") as outfile:
    dateList = []
    revenueList = []
    
# Append the data into lists
    for row in PyBank:
      dateList.append(row[0])
      revenueList.append(row[1])

# Calcuate total months
    totalMonths = len(dateList)
    print("\nFinancial Analysis\n------------")
    print(f"Total Months: {totalMonths}")
    outfile.write(f"\nFinancial Analysis\n-------\nTotal Months: {totalMonths}")

# Calculate total revenue
    sumRevenue = 0

    for revenue in revenueList:
      sumRevenue += int(revenue)

    print("Total: $" + str(sumRevenue))
    outfile.write("\nTotal: $" + str(sumRevenue))

# Calculate average change
    changeList = []
    changeSum = 0

# For Loop Average Month change

    for i in range(totalMonths-1):
	    changeValue = int(revenueList[i+1]) - int(revenueList[i])
	    changeList.append(changeValue)
	    changeSum += changeValue
      
    averageChange = changeSum/(totalMonths-1)
    print("Average Change: $" + str(averageChange))
    outfile.write("\nAverage Change $" + str(averageChange))

# Calculate greatest increase and greatest decrease in revenue

    profitChange = 0
    lossChange = 0
    for i in range(totalMonths-1):
      if changeList[i] > profitChange:
        profitChange = changeList[i]
      elif changeList[i] < lossChange:
        lossChange = changeList[i]
    

    profit = changeList.index(profitChange) + 1
    loss = changeList.index(lossChange) + 1

    print(f"Greatest Increase in Profits: {dateList[profit]} (${revenueList[profit]}")
    print(f"Greatest Decrease in Profits: {dateList[loss]} (${revenueList[loss]}")
    outfile.write(f"\nGreatest Increase in Profits: {dateList[profit]} (${revenueList[profit]})")
    outfile.write(f"\nGreatest Decrease in Profits: {dateList[loss]} (${revenueList[loss]})")