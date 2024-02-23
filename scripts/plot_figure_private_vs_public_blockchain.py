import pandas as pd
import matplotlib.pyplot as plt


# Define the file paths for the CSV files
file_paths = [
    '../data/mean/mean_private_network_1s.csv',
    '../data/mean/mean_private_network_20s.csv',
    '../data/mean/mean_public_network.csv'
]

# Define the steps and their corresponding names
steps = {
    'service_announced': 'Service\nAnnounced',
    'bid_offered': 'Bid\nOffered',
    'winner_choosen': 'Winner\nChosen',
    'deployment': 'Service\nDeployed',
    'confirm_deployment': 'Confirm\nDeployment'
}

# Set the figure size
plt.figure(figsize=(10, 6))

# Define the brew colors
colors = ['#ffffb2', '#fecc5c', '#fd8d3c', '#f03b20', '#bd0026']

# Iterate over the file paths and plot the data
for i, file_path in enumerate(file_paths):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Extract the block period from the file name, except for the last file
    if i < len(file_paths) - 1:
        block_period = file_path.split('_')[3].split('s')[0]
        block_period_label = f"Private\n(B.P.={block_period}s)"
    else:
        block_period_label = 'Public'

    # Iterate over the steps and plot the bars
    for j, step in enumerate(steps):
        # Get the mean start_time and end_time for the step
        step_data = data[data['step'] == step]
        if not step_data.empty:
            mean_start_time = step_data['start_time'].mean()
            mean_end_time = step_data['end_time'].mean()
            mean_duration = mean_end_time - mean_start_time
        else:
            mean_start_time = 0
            mean_duration = 0

        # Create the horizontal bar chart with the specified color
        plt.barh(block_period_label, mean_duration, left=mean_start_time, height=0.4, edgecolor='black', color=colors[j])


# Set the title and axis labels
plt.title('Private vs Public', fontsize=30)
plt.xlabel('Time (s)', fontsize=34)
# plt.ylabel('Blockchain networks', fontsize=28)

# Set the y-axis limits
plt.ylim(-1, len(file_paths))

plt.xticks(fontsize=35)
plt.yticks(fontsize=30)

# Invert the y-axis
plt.gca().invert_yaxis()

# Create custom legend handles and labels with step names and colors
legend_handles = [plt.Rectangle((0, 0), 1, 1, edgecolor='black', facecolor=colors[j]) for j in range(len(steps))]
legend_labels = list(steps.values())

# Add the legend below the plot
plt.legend(legend_handles, legend_labels, loc='upper left', ncol=len(steps), fontsize=23)

# Add a grid
plt.grid(True, alpha=0.3)

# Show the chart
plt.show()




