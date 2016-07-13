from textbox import TextBox
import psycopg2
from picture import Picture
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

connect_str = "dbname = 'makaimark' user = 'makaimark' host = 'localhost' password = '920410'"
conn = psycopg2.connect(connect_str)
# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to INSERT a record into the database.
sql_1 = "SELECT company_name, COUNT(name) FROM project \
       GROUP BY company_name"
sql_2 = "SELECT company_name, main_color FROM project"

try:
    cursor.execute(sql_1)
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

    Picture.drawer()

except Exception as e:
    print(e)
