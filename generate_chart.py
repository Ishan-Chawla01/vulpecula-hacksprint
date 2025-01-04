import matplotlib.pyplot as plt

# Sample data
categories = ['Steelwork', 'Plumbing', 'Carpentry', 'Manual work', 'Sweeping work', 'Manual labour']
values = [1500, 1600, 2000, 800, 800, 800]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
plt.xlabel('Job Categories')
plt.ylabel('Rate (INR per day)')
plt.title('Job Rates for Different Manual Work Categories')
plt.savefig('bar_chart.png')
