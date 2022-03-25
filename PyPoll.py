import csv
import os

file_to_load = "Resources\election_results.csv"
election_data = open(file_to_load, 'r')
#file_to_load.close()

with open(file_to_load) as election_data:
    print(election_data)

os.path.join("Resources", "election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:
    print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")
outfile = open(file_to_save, "w")
outfile.write("arapahoe")
outfile.close()

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in Election\n")
    txt_file.write("----------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")

with open(file_to_load) as election_data:
    file_reader = (election_data)   
    headers = next(file_reader)
    print(headers)






