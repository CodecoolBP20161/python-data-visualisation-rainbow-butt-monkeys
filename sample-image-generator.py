from textbox import TextBox
import psycopg2
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
'''
img = Image.new("RGB", (512, 512), "red")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("sans-serif.ttf", 16)
text_options = {
    'fill': (255, 255, 255)
}
text_content = "Sample Text"
text_size = draw.textsize(text_content)
# draw.text((x, y),text_content,(r,g,b))
draw.text((0, 0), text_content, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
img.save('sample-out.png')
'''
connect_str = "dbname = 'makaimark' user = 'makaimark' host = 'localhost' password = '920410'"
conn = psycopg2.connect(connect_str)
# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to INSERT a record into the database.
sql_1 = "SELECT company_name, COUNT(name) FROM project \
       GROUP BY company_name"
sql_2 = "SELECT company_name, main_color FROM project"

try:
    # Execute the SQL command
    # cursor.execute(sql_1)
    # Fetch all the rows in a list of lists.
    # results_1 = cursor.fetchall()
    cursor.execute(sql_2)
    results_2 = cursor.fetchall()
    dictionary = {}
    for row in results_2:
        if row[0] not in dictionary:
            dictionary.setdefault(row[0], [])
            dictionary[row[0]].append(row[1])
        else:
            dictionary.setdefault(row[0], []).append(row[1])

    # print(dictionary)
    for k, v in dictionary.items():
        v = TextBox.avg_color(v)
        print(v)
    # print(dictionary)


except Exception as e:
    print(e)
