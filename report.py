from os import listdir
from os.path import join, dirname, isfile
import pandas as pd
import sqlite3 as sql

category = dict()
sub_cat = dict()
sql_cat = dict()
sub_list = list()


def get_CSVfiles():
    """This function returns the list of CSV files from Input Directory"""

    inpath = join(dirname(__file__), 'Input')
    return [join(inpath, f) for f in listdir(inpath) if isfile(join(inpath, f)) and f[-3:] == "csv"]


def read_csv(csv_name):
    """This function returns Grouped Sub-Category dataframe in iterrows() form and frequency of Category values."""

    df = pd.read_csv(csv_name)
    # h = df.groupby(["Sub-category", "Category"]).size().reset_index(name="Count").sort_values(by='Count',ascending=False)
    sub = df.groupby(["Sub-category", "Category"]
                     ).size().reset_index(name="Count")
    cat_count = df["Category"].value_counts()
    return sub.iterrows(), cat_count


def sub_fun(loop):
    """This function stores the subcategory values frequency in dictionary named as sub_cat."""

    for index, row in loop:
        first = row["Sub-category"].strip().capitalize()
        second = row["Category"].strip().capitalize()
        total = f"{first}@{second}"
        if total in sub_cat:
            sub_cat[total] += row["Count"]
        else:
            sub_cat[total] = row["Count"]
    return


def cat_fun(loop):
    """This function stores the Category values frequency in dictionary named as category."""

    for t, v in loop.items():
        k = t.strip().capitalize()
        if k in category:
            category[k] += int(v)
        else:
            category[k] = int(v)
    return


def freqeuncy(docs):
    """This function iterates the list of CSV files and do the sub_fun() and cat_fun() for every CSV file."""

    for doc in docs:
        sub, cat = read_csv(doc)
        sub_fun(sub)
        cat_fun(cat)
    return


def cat_sql(data):
    """
        Creates a Category table in Report database and stores the required values like 
        Category and frequency of Category.
    """

    con = sql.connect('report.db')
    c = con.cursor()
    c.execute("""CREATE TABLE categories (
        category text,
		count integer
		)""")
    con.commit()
    c.executemany("INSERT INTO categories VALUES (?, ?)", list(data.items()))
    con.commit()
    con.close()
    return


def sub_sql(data):
    """
        Creates a Sub-Category table in Report database and stores the required values like
        Sub-Category, frequency of Sub-Category, Category and Category ID.
    """

    con = sql.connect('report.db')
    c = con.cursor()
    c.execute("""CREATE TABLE subcategory (
		sub_category text,
		count integer,
        category text,
        category_id integer
		)""")
    con.commit()
    c.executemany("INSERT INTO subcategory VALUES (?, ?, ?, ?)", data)
    con.commit()
    con.close()
    return


def fetch_cat_sql():
    """
        Fetches the data from Category table and 
        returns a list with unique ID & Data and a list of without Unqiue ID.
    """

    con = sql.connect('report.db')
    c = con.cursor()
    c.execute("SELECT rowid, category FROM categories")
    data_fetched1 = c.fetchall()
    con.commit()
    c.execute("SELECT * FROM categories")
    data_fetched2 = c.fetchall()
    con.commit()
    con.close()
    return data_fetched1, data_fetched2


def fetch_sub_sql():
    """
        Fetches the data from Sub-Category table and 
        returns a list with unique ID & Data and a list of without Unqiue ID.
    """

    con = sql.connect('report.db')
    c = con.cursor()
    c.execute("SELECT rowid, sub_category FROM subcategory")
    data_fetched1 = c.fetchall()
    con.commit()
    c.execute("SELECT * FROM subcategory")
    data_fetched2 = c.fetchall()
    con.commit()
    con.close()
    return data_fetched1, data_fetched2


def list_sub(cat_data, sub_data, l):
    """This function stores the tuple(SubCategory, SubCategoryFrequency, Category, Category ID) in the sub_list[]"""

    for k, v in sub_data.items():
        s, c = k.split('@')
        l.append((s, v, c, cat_data[c]))
    return


def list_cat(category_sql_data):
    """This function maps the Category's ID with Category and stores in Dictionary names sql_cat."""

    for rowid, categoryName in cat_rowid:
        sql_cat[categoryName] = rowid


if __name__ == "__main__":
    documents = get_CSVfiles()
    freqeuncy(documents)
    cat_sql(category)
    cat_rowid, catsql_data = fetch_cat_sql()
    list_cat(cat_rowid)
    list_sub(sql_cat, sub_cat, sub_list)
    sub_sql(sub_list)
    sub_rowid, subsql_data = fetch_sub_sql()

    # print(cat_rowid)
    # print("\n", sub_rowid)
