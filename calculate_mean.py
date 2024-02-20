import os
import pandas as pd

def calculate_mean_values(directory, file_prefix, output_file):
    # Initialize dictionaries to store the sums and counts for start_time and end_time
    sum_start_times = {}
    sum_end_times = {}
    count_steps = {}

    # Iterate over each test sample directory
    for test_dir in os.listdir(directory):
        test_path = os.path.join(directory, test_dir)
        if os.path.isdir(test_path):
            # Read the CSV file for each test
            file_path = os.path.join(test_path, f'{file_prefix}.csv')
            df = pd.read_csv(file_path)

            # Iterate over each row in the DataFrame
            for _, row in df.iterrows():
                step = row['step']
                start_time = row['start_time']
                end_time = row['end_time']

                # Update the sum of start_time and end_time for the step
                sum_start_times[step] = sum_start_times.get(step, 0) + start_time
                sum_end_times[step] = sum_end_times.get(step, 0) + end_time

                # Increment the count for the step
                count_steps[step] = count_steps.get(step, 0) + 1

    # Create a new DataFrame to store the mean values
    result_data = []

    # Iterate over the steps and calculate the mean values
    for step in sum_start_times.keys():
        mean_start_time = sum_start_times[step] / count_steps[step]
        mean_end_time = sum_end_times[step] / count_steps[step]
        result_data.append({'step': step, 'start_time': mean_start_time, 'end_time': mean_end_time})

    # Create the result DataFrame
    result_df = pd.DataFrame(result_data, columns=['step', 'start_time', 'end_time'])

    # Save the result DataFrame to a new CSV file
    result_df.to_csv(output_file, index=False)
    print(f'Results saved to {output_file}')

def main():
    choice = input("Calculate mean values for:\n1. Private Network\n2. Public Network\nEnter your choice (1 or 2): ")
    if choice == "1":
        periods = ['0s', '1s', '2s', '5s', '10s', '20s']
        for period in periods:
            directory = f'private_network_{period}'
            output_file = f"mean/mean_private_network_{period}.csv"
            calculate_mean_values(directory, 'federation_private_network', output_file)
    elif choice == "2":
        directory = 'public_network'
        output_file = "mean/mean_public_network.csv"
        calculate_mean_values(directory, 'federation_public_network', output_file)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
