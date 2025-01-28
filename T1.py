import os
import re
import pandas as pd


def search_bootstrap_classes(directory, bootstrap_class):
    results = []

    # Walk through all files in the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Check if the file is readable (e.g., .html, .css, .js, etc.)
            if file.endswith(('.jsp', '.css', '.js')):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                        # Search each line for the Bootstrap class
                        for line_number, line in enumerate(lines, start=1):
                            if bootstrap_class in line:
                                matches = re.findall(rf'\b{bootstrap_class}\b', line)
                                if matches:
                                    results.append({
                                        'File Name': file_path,
                                        'Line Number': line_number,
                                        'Class Found': ', '.join(matches),
                                    })
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    return results


def export_to_excel(data, output_file):
    # Convert the data to a DataFrame and export to Excel
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Results exported to {output_file}")


def main():

    # Specify the directory to search and the Bootstrap class to find
    directory_to_search = "/home/abhishek/Documents/proj1"
    bootstrap_class_to_find = "modal"
    output_excel_file = "bootstrap_class_results.xlsx"

    # Search for the Bootstrap class and export results
    results = search_bootstrap_classes(directory_to_search, bootstrap_class_to_find)
    if results:
        export_to_excel(results, output_excel_file)
    else:
        print("No matches found for the specified Bootstrap class.")

if __name__ == "__main__":
    main()