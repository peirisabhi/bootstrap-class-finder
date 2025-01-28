import os
import re
import pandas as pd

def main():
    print("Welcome to T2!")
    for root, _, files in os.walk("/home/abhishek/Documents/proj1"):
        print(files)
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)

if __name__ == "__main__":
    main()