import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the file paths for the CSV files
file_paths = [
    'mean/mean_private_network_1s.csv',
    'mean/mean_private_network_2s.csv',
    'mean/mean_private_network_5s.csv',
    'mean/mean_private_network_10s.csv',
    'mean/mean_private_network_20s.csv'
]

# Define the steps and their corresponding names, including 'federation_completed'
steps = {
    'service_announced': 'Service\nAnnounced',
    'bid_offered': 'Bid\nOffered',
    'winner_choosen': 'Winner\nChosen',
    'deployment': 'Service\nDeployed',
    'confirm_deployment': 'Confirm\nDeployment',
    'federation_completed': 'Federation\nCompleted'
}

# Set the figure size
plt.figure(figsize=(12, 8))

# Define the block periods
block_periods = [1, 2, 5, 10, 20]

# Set the width of each bar
bar_width = 0.15

# Define the colors for each block period
colors = ['#fecc5c', '#fd8d3c', '#f03b20', '#bd0026', '#800026']  # Adjusted for 5 colors

# Initialize legend handles
legend_handles = []

# Iterate over the file paths and plot the data
for i, file_path in enumerate(file_paths):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Initialize the array of durations for each step
    durations = []

    # Calculate federation_completed duration as the difference between the earliest start and the latest end
    federation_start = data['start_time'].min()
    federation_end = data['end_time'].max()
    federation_completed_duration = federation_end - federation_start

    # Iterate over the steps
    for step in steps.keys():
        if step != 'federation_completed':
            step_data = data[data['step'] == step]
            if not step_data.empty:
                mean_duration = step_data['end_time'].mean() - step_data['start_time'].mean()
            else:
                mean_duration = 0
            durations.append(mean_duration)
        else:
            durations.append(federation_completed_duration)  # Append federation_completed duration

    # Calculate the x-coordinate for each bar
    x = np.arange(len(steps)) + i * bar_width

    # Plot the bar chart
    plt.bar(x, durations, width=bar_width, color=colors[i], edgecolor='black', linewidth=1, label=f'{block_periods[i]}s')

    # Append the bar to the legend handles
    legend_handles.append(plt.Rectangle((0, 0), 1, 1, color=colors[i]))

# Set the x-axis ticks and labels with increased font size
plt.xticks(np.arange(len(steps)) + bar_width * (len(file_paths) - 1) / 2, [steps[step] for step in steps], fontsize=35)

plt.yticks(fontsize=44)

# Set the title and axis labels with increased font size
plt.title('Mean Federation process duration on a private blockchain', fontsize=30)
plt.xlabel('Steps', fontsize=34)
plt.ylabel('Time (s)', fontsize=34)

# Add the legend to the upper-left corner with increased font size
legend = plt.legend(legend_handles, ['B.P.={}s'.format(period) for period in block_periods], loc='upper left', ncol=len(file_paths), fontsize=30)

# Set the border color and width for the legend handles
for handle in legend.legendHandles:
    handle.set_edgecolor('black')
    handle.set_linewidth(1)

# Add a grid
plt.grid(True, alpha=0.3)

# Show the chart
plt.show()
