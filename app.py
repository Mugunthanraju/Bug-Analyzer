import sqlite3 as sql
from flask import Flask
from flask import render_template

app = Flask(__name__)


def fetch_cat_sql():
    """
        This function fetches the values from categories Table in report database.
    """

    con = sql.connect('report.db')
    c = con.cursor()
    c.execute("SELECT rowid, * FROM categories")
    # c.execute("SELECT * FROM categories")
    data_fetched = c.fetchall()
    con.commit()
    con.close()
    return tuple(data_fetched)


def fetch_sub_sql():
    """
        This function fetches the values from subcategory Table in report database.
    """

    con = sql.connect('report.db')
    c = con.cursor()
    # c.execute("SELECT rowid, * FROM subcategory")
    # c.execute("SELECT * FROM subcategory")
    # c.execute("SELECT sub_category, count, category FROM subcategory ORDER BY count DESC")
    c.execute("SELECT sub_category, count, category FROM subcategory")
    data_fetched = c.fetchall()
    con.commit()
    con.close()
    return tuple(data_fetched)


def cat_sub(cid):
    """
        This function fetches the data from table subcategory of Category ID which matches with given parameter ID.
    """

    sub_category
    con = sql.connect('report.db')
    c = con.cursor()
    c.execute(
        f"SELECT sub_category, COUNT(sub_category) FROM subcategory GROUP by sub_category HAVING category_id = {cid}")
    data_fetched = c.fetchall()
    con.commit()
    con.close()
    return tuple(data_fetched)


def cat_name(cid):
    """
        This function fetches the category_name from table categories of Unique ID which matches with given parameter ID.
    """

    sub_category
    con = sql.connect('report.db')
    c = con.cursor()
    c.execute(f"SELECT DISTINCT category FROM categories WHERE rowid = {cid}")
    data_fetched = c.fetchall()
    con.commit()
    con.close()
    return data_fetched


@app.route('/')
def category():
    cat_head = ("Index", "CategoryName", "CategoryCount")
    cat_data = fetch_cat_sql()
    return render_template("category.html", headings=cat_head, data=cat_data)


@app.route("/<int:c_id>")
def cat_sub_list(c_id):
    cat_sub_data = cat_sub(c_id)
    cateogry_name = tuple(cat_name(c_id))
    return render_template("cat_sub.html", cat=cateogry_name, data=cat_sub_data)


@app.route('/sub')
def sub_category():
    sub_head = ("SubCategoryName", "SubCategoryCount", "CategoryName")
    sub_data = fetch_sub_sql()
    return render_template("sub.html", headings=sub_head, data=sub_data)


if __name__ == "__main__":
    app.run(debug=True)
