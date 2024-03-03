import csv
import os
import logging

def remove_bom(text):
    # Remove BOM if present
    if text.startswith('\ufeff'):
        return text[1:]
    return text

def sanitize_folder_name(name):
    # Replace special characters with space or dash
    name = name.replace('?', ' ').replace("'", ' ').replace('|', ' ').replace('/', '-').replace('\\', '-').replace(':', '-')
    return name.strip()  # Remove leading and trailing spaces

def create_folders(csv_path, column_name, target_directory, log_file):
    # Create target directory if it doesn't exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Create directory for log file if it doesn't exist
    log_directory = os.path.dirname(log_file)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Set up logging
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logger = logging.getLogger()

    total_entries = 0
    folders_created = 0

    # Open the CSV file with latin-1 encoding
    with open(csv_path, newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        # Iterate over each row in the CSV file
        for row in reader:
            # Get the value of the specified column
            folder_name = row[column_name]
            # Remove BOM if present
            folder_name = remove_bom(folder_name)
            # Sanitize folder name
            sanitized_name = sanitize_folder_name(folder_name)
            # Check if the folder name is empty
            if not sanitized_name.strip():
                continue

            total_entries += 1

            # Check if folder already exists
            folder_path = os.path.join(target_directory, sanitized_name)
            if os.path.exists(folder_path):
                message = f"Folder '{sanitized_name}' already exists"
                print(message)
                logger.info(message)
                continue

            # Attempt to create the directory
            try:
                os.makedirs(folder_path)
                folders_created += 1
                message = f"Created folder: {folder_path}"
                print(message)
                logger.info(message)
            except Exception as e:
                error_message = f"Error creating folder '{sanitized_name}': {str(e)}"
                print(error_message)
                logger.error(error_message)

    # Log the summary message
    summary_message = f"Out of {total_entries} entries, {folders_created} folders are created."
    print(summary_message)
    logger.info(summary_message)

    # Remove the handler at the end to avoid duplicate logs
    logger.removeHandler(logging.getLogger().handlers[0])

def validate_path(prompt):
    while True:
        path = input(prompt)
        if os.path.exists(path):
            return path
        else:
            print("The specified path does not exist. Please provide a valid path.")

if __name__ == "__main__":
    # Prompt user for input
    csv_path = validate_path("Enter the path to the CSV file: ")
    column_name = input("Enter the name of the column containing folder names: ")
    target_directory = input("Enter the target directory where folders will be created: ")
    log_file = input("Enter the path to the log file: ")

    # Call the function to create folders
    create_folders(csv_path, column_name, target_directory, log_file)
