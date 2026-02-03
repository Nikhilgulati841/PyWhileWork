import numpy as np

# sales=np.array([100, 200, 300, 400,12,345,257,346,567,35,647,578,58,578,5464,345,2345,2345,234,2345,2345])
# cost=np.array([80, 150, 250, 350])
# profit=sales - cost
# tax=profit * 0.1 # 18% tax
# net_profit=profit - tax
# avg_profit=np.mean(net_profit)
# print("Sales:", sales)
# print("Cost:", cost)    
# print("Profit:", profit)
# print("Tax:", tax)
# print("Net Profit:", net_profit)
# print("Average Net Profit:", avg_profit)
# print("Manually avg_profit:",(18+45+45+45)/4)

sales=np.array([95,100,105])

total_sales=np.sum(sales)
print("Total Sales:", total_sales)
avg_sales=np.mean(sales)
print("Average Sales:",avg_sales)
middle_sales=np.median(sales)
print("Middle Sales:",middle_sales) 
minimum_sales=np.min(sales)
print("Minimum Sales:",minimum_sales)
maximum_sales=np.max(sales)
print("Maximum Sales:",maximum_sales)
std_dev_sales=np.std(sales)
print("Standard Deviation of Sales:",std_dev_sales)
sorted_sales=np.sort(sales)
print("Sorted Sales:",sorted_sales)
counts=np.unique(sales, return_counts=True)
print("Unique Sales and their counts:",counts)

cv=(std_dev_sales/avg_sales)*100
print(f"CV : {cv:.2f}%")
