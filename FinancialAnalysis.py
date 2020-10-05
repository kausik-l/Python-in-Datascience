
"""
author : Kausik Lakkaraju

Source for data : https://www.superdatascience.com/pages/python
"""




import statistics
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
profit = list(range(12))
for i in range(len(revenue)):
    profit[i] = revenue[i] - expenses[i]
for i in range(len(profit)):
    print("Profit for",months[i], "is",profit[i])
pat = list(range(len(profit)))
for i in range(len(profit)):
    pat[i] = profit[i] - ((30/100)*profit[i])
print("\n")
for i in range(len(profit)):
    print("Profit after tax for",months[i],"is",pat[i])
margin = list(range(12))
for i in range(len(margin)):
    margin[i] = pat[i]/revenue[i]
print("\n")
for i in range(len(profit)):
    print("Margin for",months[i],"is",margin[i])
print("\n")
for i in range(len(profit)):
    if(pat[i]>statistics.mean(pat)):
        print(months[i],"is a good month")
    else:
        print(months[i],"is a bad month")
print("\n\n")
for i in range(len(profit)):
    if(pat[i] == max(pat)):
        print(months[i],"is the best year,afterall")
