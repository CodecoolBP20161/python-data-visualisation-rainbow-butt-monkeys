from textbox import TextBox
import psycopg2
from picture import Picture, Picture_2
from project_names_by_currency import ProjectByCurrency
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

connect_str = "dbname = 'makaimark' user = 'makaimark' host = 'localhost' password = '920110'"
conn = psycopg2.connect(connect_str)
# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to INSERT a record into the database.
sql_1 = "SELECT company_name, COUNT(name) FROM project \
       GROUP BY company_name"
sql_2 = "SELECT company_name, main_color FROM project"
sql_3 = "SELECT name, budget_value, budget_currency, main_color FROM project;"

try:
    # Execute the SQL command
    cursor.execute(sql_1)
    # Fetch all the rows in a list of lists.
    results_1 = cursor.fetchall()
    cursor.execute(sql_2)
    results_2 = cursor.fetchall()
    dictionary = {}
    for row in results_2:
        if row[0] not in dictionary:
            dictionary.setdefault(row[0], [])
            dictionary[row[0]].append(row[1])
        else:
            dictionary.setdefault(row[0], []).append(row[1])

    for k, v in dictionary.items():
        dictionary[k] = TextBox.avg_color(v)

    for i in results_1:
        if i[1] != 0:
            for k, v in dictionary.items():
                if i[0] == k:
                    Picture.add_to_textboxes(dictionary[k], 25*int(i[1]), k)

    # print(Picture.list_of_textboxes[5].color, Picture.list_of_textboxes[5].size, Picture.list_of_textboxes[5].company_name)
    Picture.drawer()

except Exception as e:
    print(e)

def projects_by_currency():
    try:
        cursor.execute(sql_3)
        # Fetch all the rows in a list of lists.
        results_1 = cursor.fetchall()
        all_companies = []
        for row in results_1:
            if row[0] not in all_companies:
                company = []
                company.append(row[0])
                company.append(float(row[1]))
                company.append(row[2])
                company.append(row[3])
                all_companies.append(company)
            else:
                pass
        result = ProjectByCurrency.make_reverse_order(all_companies)
        for i in result:
           i[2] = TextBox.hex_to_rgb(i[2])

        for i in result:
            Picture_2.add_to_textboxes(i[0], i[2], i[1])
            print(i)
        Picture_2.drawer()

    except Exception as e:
        print(e)

projects_by_currency()