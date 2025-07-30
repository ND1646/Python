import matplotlib.pyplot as plt

# Sample data
categories = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
values = [90, 80, 60, 70, 50]

# Custom bar colors
colors = ['#FF5733', '#33FFCE', '#FF33F6', '#85FF33', '#335BFF']

# Plot bar chart with custom colors and outline
plt.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)

#  Add value labels on top of each bar
for i, v in enumerate(values):
    plt.text(i, v + 2, str(v), ha='center', fontweight='bold')

# Titles and labels
plt.title(" 🧠 Programming Language Popularity", fontsize=14)
plt.xlabel("Languages", fontsize=12)
plt.ylabel("Popularity Score", fontsize=12)

# Save the chart
plt.savefig("bar_chart_colored.png", dpi=300, facecolor="white")

# Show it
plt.show()
