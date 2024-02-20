import pandas as pd
import os

def merge_and_format_csv_files(input_file1, input_file2, output_file):
    # Read the input CSV files
    consumer_df = pd.read_csv(input_file1)
    provider_df = pd.read_csv(input_file2)
    merged_df = pd.concat([consumer_df, provider_df], ignore_index=True)

    # Order of steps
    order = [
        'serviceAnnouncementSent',
        'serviceAnnouncementReceived',
        'bidOfferSent',
        'bidOfferReceived',
        'choosingProvider',
        'providerChoosen',
        'winnerChoosenSent',
        'winnerChoosenReceived',
        'deploymentStart',
        'deploymentFinished',
        'confirmDeploymentSent',
        'confirmDeploymentReceived'
    ]

    # Reorder and sort by timestamp
    merged_df = merged_df[merged_df['step'].isin(order)].sort_values('timestamp')

    # Define the mappings between steps and their corresponding new format
    step_indices = {
        'service_announced': ['serviceAnnouncementSent', 'serviceAnnouncementReceived'],
        'bid_offered': ['bidOfferSent', 'bidOfferReceived'],
        'winner_choosen': ['choosingProvider', 'winnerChoosenReceived'],
        'deployment': ['deploymentStart', 'deploymentFinished'],
        'confirm_deployment': ['confirmDeploymentSent', 'confirmDeploymentReceived']
    }

    # Format the merged data
    formatted_data = []
    for step, (start_step, end_step) in step_indices.items():
        start_time = merged_df[merged_df['step'] == start_step]['timestamp'].min()
        end_time = merged_df[merged_df['step'] == end_step]['timestamp'].max()
        formatted_data.append({'step': step, 'start_time': start_time, 'end_time': end_time})

    formatted_df = pd.DataFrame(formatted_data)
    formatted_df.to_csv(output_file, index=False)

    # Display the formatted DataFrame
    print(formatted_df)

def process_network(directory, poa_delays):
    for delay in poa_delays:
        # Adjust base_directory construction to avoid adding an underscore when delay is empty
        base_directory = f"{directory}_{delay}" if delay else directory

        for i in range(1, 21):
            # Make sure file paths are constructed correctly
            consumer_file = os.path.join(base_directory, f"test_{i}/federation_{directory}_consumer.csv")
            provider_file = os.path.join(base_directory, f"test_{i}/federation_{directory}_provider.csv")
            merged_file = os.path.join(base_directory, f"test_{i}/federation_{directory}.csv")

            merge_and_format_csv_files(consumer_file, provider_file, merged_file)
            print(f"Formatted DataFrame for test_{i} in {base_directory}.")


def main():
    while True:
        print("1. Private Network")
        print("2. Public Network")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            directory = 'private_network'
            poa_delays = ['0s', '1s', '2s', '5s', '10s', '20s']
            process_network(directory, poa_delays)
            break
        elif choice == "2":
            directory = 'public_network'
            # For the public network, process without multiple delays
            process_network(directory, [''])
            break
        elif choice == "0":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
