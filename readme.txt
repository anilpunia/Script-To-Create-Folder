Prerequisites

1. Python: The script is written in Python, so you need to have Python installed on your system. You can download Python from the official website: Python Downloads. Make sure to install Python version 3.x.

2. CSV Module: The script uses the csv module, which is a built-in module in Python, so no additional installation is required.

3. Logging Module: The script uses the logging module to log messages to a file. This module is also a built-in module in Python, so no additional installation is required.

4. Operating System: The script is designed to run on any operating system supported by Python, including Windows, macOS, and Linux.

Once you have Python installed on your system, you can run the script using the Python interpreter. If you're using Windows, you can run the script from the Command Prompt.

After ensuring that you have Python installed and the required modules available, you can follow the steps mentioned below in the "How to run" to run the script successfully.

How to run

1. Prepare CSV File: Ensure you have a CSV file containing the data you want to process. The CSV file should have at least one column containing the names of the folders you want to create. The cell values under the target column should be in format <Application Name>_<Application UUID> to identify the application uniquely. 

2. Open Terminal or Command Prompt: Navigate to the directory where you saved the Python script and the CSV file.

3. Run the Script: In the terminal or command prompt, type python script_name.py and press Enter. Replace script_name.py with the name of the Python script file you downloaded.

4. Follow the Prompts: The script will prompt you to enter the required information, such as the path to the CSV file, the name of the column containing folder names, the target directory where folders will be created, and the path to the log file.

5. Provide Input: Enter the requested information as prompted by the script and press Enter after each input.

6. Execution: The script will then process the CSV file, create folders based on the specified column, and log the process in the specified log file.

7. Review Output: Once the script completes execution, you can review the folders created in the specified target directory and check the log file for any messages or errors encountered during the process.

By following these steps, you can run the Python script to create folders based on the data in the CSV file.

Command line Usage

Python csv_folder_creator.py
Enter the path to the CSV file: C:\xxxxx\<csvName>.csv
Enter the name of the column containing folder names: <Column_Name>
Enter the target directory where folders will be created: C:\xxxx\<target folder name>
Enter the path to the log file: C:\xxxx\<log location>\log.log

