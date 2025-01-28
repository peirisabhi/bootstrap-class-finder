import os
import re
import pandas as pd


def search_bootstrap_classes(directory, bootstrap_classes):
    results = []

    # Create a regex pattern to match any of the provided classes
    class_pattern = r'\b(' + '|'.join(re.escape(cls) for cls in bootstrap_classes) + r')\b'
    print(class_pattern)
    # Walk through all files in the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Check if the file is readable (e.g., .html, .css, .js, etc.)
            if file.endswith(('.jsp', '.js')):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                        # Search each line for any of the Bootstrap classes
                        for line_number, line in enumerate(lines, start=1):
                            matches = re.findall(class_pattern, line)
                            if matches:
                                results.append({
                                    'File Name': file_path,
                                    'Line Number': line_number,
                                    'Classes Found': ', '.join(matches),
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

    directory_to_search = "/home/abhishek/Documents/proj1"
    bootstrap_class_to_find = "modal,fade,text-center,mt-4"
    output_excel_file = "bootstrap_class_results.xlsx"

    # Split the classes by comma and strip whitespace
    bootstrap_classes = [cls.strip() for cls in bootstrap_class_to_find.split(',')]
    print(bootstrap_classes)
    # Search for the Bootstrap classes and export results
    results = search_bootstrap_classes(directory_to_search, bootstrap_classes)
    if results:
        export_to_excel(results, output_excel_file)
    else:
        print("No matches found for the specified Bootstrap classes.")


if __name__ == "__main__":
    main()
