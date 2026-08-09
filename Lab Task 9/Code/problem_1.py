import os
import matplotlib
matplotlib.use('Agg') # Non-interactive backend to save plots directly
import matplotlib.pyplot as plt
import pandas as pd

# Create Output directory if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), "..", "Output")
os.makedirs(output_dir, exist_ok=True)

# Load Titanic Dataset
dataset_path = os.path.join(os.path.dirname(__file__), "..", "titanic.csv")
if not os.path.exists(dataset_path):
    dataset_path = "titanic.csv"

df = pd.read_csv(dataset_path)

# Fill missing values for plotting
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# 1. Line Plot (Fare trend across first 50 passengers)
plt.figure(figsize=(8, 5))
plt.plot(df.index[:50], df["Fare"][:50], color="#2b5c8f", marker="o", linewidth=2, label="Ticket Fare")
plt.title("Line Plot: Ticket Fare Trend (First 50 Passengers)", fontsize=14, fontweight="bold")
plt.xlabel("Passenger Index", fontsize=12)
plt.ylabel("Fare ($)", fontsize=12)
plt.legend()
plt.tight_layout()
line_plot_path = os.path.join(output_dir, "line_plot.png")
plt.savefig(line_plot_path, dpi=300)
plt.close()
print(f"Saved: {line_plot_path}")

# 2. Scatter Plot (Age vs Fare)
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Fare"], alpha=0.6, c=df["Survived"], cmap="coolwarm", edgecolors="w", s=50)
plt.title("Scatter Plot: Age vs Ticket Fare", fontsize=14, fontweight="bold")
plt.xlabel("Age (Years)", fontsize=12)
plt.ylabel("Fare ($)", fontsize=12)
plt.colorbar(label="Survived (0 = No, 1 = Yes)")
plt.tight_layout()
scatter_plot_path = os.path.join(output_dir, "scatter_plot.png")
plt.savefig(scatter_plot_path, dpi=300)
plt.close()
print(f"Saved: {scatter_plot_path}")

# 3. Bar Chart (Passenger Count by Passenger Class)
plt.figure(figsize=(8, 5))
pclass_counts = df["Pclass"].value_counts().sort_index()
bars = plt.bar(["Class 1", "Class 2", "Class 3"], pclass_counts, color=["#4c72b0", "#55a868", "#c44e52"], width=0.5)
plt.title("Bar Chart: Passenger Count by Class", fontsize=14, fontweight="bold")
plt.xlabel("Passenger Class", fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha="center", va="bottom", fontweight="bold")
plt.tight_layout()
bar_chart_path = os.path.join(output_dir, "bar_chart.png")
plt.savefig(bar_chart_path, dpi=300)
plt.close()
print(f"Saved: {bar_chart_path}")

# 4. Histogram (Age Distribution)
plt.figure(figsize=(8, 5))
plt.hist(df["Age"], bins=20, color="#8172b0", edgecolor="black", alpha=0.7)
plt.title("Histogram: Age Distribution of Passengers", fontsize=14, fontweight="bold")
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.tight_layout()
histogram_path = os.path.join(output_dir, "histogram.png")
plt.savefig(histogram_path, dpi=300)
plt.close()
print(f"Saved: {histogram_path}")

# 5. Pie Chart (Survival Proportions)
plt.figure(figsize=(7, 7))
survival_counts = df["Survived"].value_counts()
labels = ["Deceased (0)", "Survived (1)"]
colors = ["#ff9999", "#66b3ff"]
plt.pie(survival_counts, labels=labels, autopct="%1.1f%%", startangle=140, colors=colors, explode=(0.05, 0), textprops={'fontsize': 12, 'weight': 'bold'})
plt.title("Pie Chart: Survival Rate Proportion", fontsize=14, fontweight="bold")
plt.tight_layout()
pie_chart_path = os.path.join(output_dir, "pie_chart.png")
plt.savefig(pie_chart_path, dpi=300)
plt.close()
print(f"Saved: {pie_chart_path}")

# 6. Combined Subplots Grid (2x3 Grid)
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Titanic Dataset Visualization Overview (Lab 09 Subplots)", fontsize=16, fontweight="bold")

# Subplot 1: Line Plot
axes[0, 0].plot(df.index[:50], df["Fare"][:50], color="#2b5c8f", marker="o")
axes[0, 0].set_title("Line Plot: Fare Trend (50 Pass.)")
axes[0, 0].set_xlabel("Index")
axes[0, 0].set_ylabel("Fare ($)")

# Subplot 2: Scatter Plot
axes[0, 1].scatter(df["Age"], df["Fare"], alpha=0.5, c="#ccb974")
axes[0, 1].set_title("Scatter Plot: Age vs Fare")
axes[0, 1].set_xlabel("Age")
axes[0, 1].set_ylabel("Fare ($)")

# Subplot 3: Bar Chart
axes[0, 2].bar(["Class 1", "Class 2", "Class 3"], pclass_counts, color=["#4c72b0", "#55a868", "#c44e52"])
axes[0, 2].set_title("Bar Chart: Passenger Class")
axes[0, 2].set_ylabel("Count")

# Subplot 4: Histogram
axes[1, 0].hist(df["Age"], bins=15, color="#8172b0", edgecolor="black")
axes[1, 0].set_title("Histogram: Age Distribution")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Frequency")

# Subplot 5: Pie Chart
axes[1, 1].pie(survival_counts, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
axes[1, 1].set_title("Pie Chart: Survival Rate")

# Subplot 6: Box Plot of Age by Pclass
df.boxplot(column="Age", by="Pclass", ax=axes[1, 2], patch_artist=True)
axes[1, 2].set_title("Box Plot: Age by Class")

plt.tight_layout()
plt.subplots_adjust(top=0.92)
subplots_path = os.path.join(output_dir, "subplots_output.png")
plt.savefig(subplots_path, dpi=300)
plt.close()
print(f"Saved: {subplots_path}")
