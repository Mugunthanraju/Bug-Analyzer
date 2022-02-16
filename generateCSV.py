"""
Store the input CSV files in the Input Directory.
Output CSV files are generated in Output Directory.
"""

from datetime import date
from os import listdir
from os.path import join, dirname, isfile
import pandas as pd
import csv


def get_CSVfiles():
    inpath = join(dirname(__file__), 'Input')
    return [join(inpath, f) for f in listdir(inpath) if isfile(join(inpath, f)) and f[-3:] == "csv"]


def read_csv(csv_name, column_name='Category'):
    df = pd.read_csv(csv_name)
    count = df[column_name].value_counts()
    return count


def freq_dict(docs, column_name):
    freq = dict()
    for doc in docs:
        count_dict = read_csv(doc, column_name)
        for t, v in count_dict.items():
            k = t.strip().capitalize()
            if k in freq:
                freq[k] += int(v)
            else:
                freq[k] = int(v)
    return freq


def write_csv(frequency, outpath, column_name):
    day = date.today().strftime('%d-%m-%Y')
    with open(join(outpath, f'CategoryFrequency-({day}).csv'), 'w', encoding='UTF8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([column_name, "Frequency"])
        for key, value in frequency.items():
            writer.writerow([key, value])
    csv_file.close()
    print(f'{column_name}Frequency-({day}).csv -> Created')
    return


def generate_frequency(csv_files, column_name="Category"):
    count = freq_dict(csv_files, column_name)
    outpath = join(dirname(__file__), 'Output')
    write_csv(count, outpath, column_name)
    return


if __name__ == "__main__":

    csv_files = get_CSVfiles()
    # column_name = input("Enter the column name : ")
    generate_frequency(csv_files)


# columns = ["Category"]
# df = pd.read_csv("input.csv", usecols=columns)
# count = df.groupby(['Category']).count()
# print(type(count))
# print(count)
# print(df.head())
# for i, v in dict(count).items():
