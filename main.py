import os
import shutil
import csv

# Create a text file
with open("log.txt", "w") as file:
    file.write("Student records generated successfully.\n")
    file.write("Date: 12-06-2026")

print("Log file created.")

# Read the text file
with open("log.txt", "r") as file:
    print(file.read())
