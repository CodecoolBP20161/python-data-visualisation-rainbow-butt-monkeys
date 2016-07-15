from textbox import TextBox
import config
import psycopg2
from picture import Picture
from project_names_by_currency import ProjectByCurrency
from companies_by_maintenance import CompaneiesByMaintenance
from PIL import Image


connect_str = "dbname = '%s' user = '%s' host = '%s' password = '%s'" % (config.dbname, config.name, config.host, config.password)
conn = psycopg2.connect(connect_str)
# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to INSERT a record into the database.
sql_1 = "SELECT company_name, COUNT(name) FROM project \
       GROUP BY company_name"
sql_2 = "SELECT company_name, main_color FROM project"
sql_3 = "SELECT name, budget_value, budget_currency, main_color FROM project;"
sql_4 = """SELECT "name", company_name, maintenance_requested, main_color FROM project"""
sql_5 = "SELECT company_name, COUNT(manager) FROM project GROUP BY company_name"
sql_6 = "SELECT company_name, main_color FROM project"
sql_7 = """SELECT "name", main_color FROM project WHERE status = 4"""

def project_name_by_status():
    try:
        cursor.execute(sql_7)
        results_7 = cursor.fetchall()
        dictionary = {}
        for row in results_7:
            if row[0] not in dictionary and row[0] != None:
                dictionary.setdefault(row[0], [])
                dictionary[row[0]].append(row[1])

        for k, v in dictionary.items():
            dictionary[k] = TextBox.avg_color(v)

        for k, v in dictionary.items():
            Picture.add_to_textboxes(v, 50, k)

        Picture.drawer("project_name_by_status.png")

    except Exception as e:
        print(e)


def companies_by_project_number():
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
                        Picture.add_to_textboxes(dictionary[k], 15*int(i[1]), k)

        Picture.drawer("companies_by_project_number.png")

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
            Picture.add_to_textboxes(i[2], i[1], i[0])
            # print(i)
        Picture.drawer('projects_by_currency.png')

    except Exception as e:
        print(e)


def companies_by_maintenance():
    try:
        cursor.execute(sql_4)
        all_data = cursor.fetchall()
        all_companies = []
        for row in all_data:
            if row[0] != None:
                actual_line = []
                actual_line.append(row[0])
                actual_line.append(row[1])
                actual_line.append(row[2])
                actual_line.append(row[3])
                all_companies.append(actual_line)

        company_objects = []
        for i in all_companies:
            actual = CompaneiesByMaintenance(i[0], i[1], i[2], i[3])
            company_objects.append(actual)

        result = CompaneiesByMaintenance.output_maker(company_objects)

        for i in result:
            Picture.add_to_textboxes(i[1], i[2], i[0])
            # print(i)
        Picture.drawer("companies_by_maintenance.png")

    except Exception as e:
        print(e)


def companies_by_manager_number():
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
                        Picture.add_to_textboxes(dictionary[k], 10*int(i[1]), k)

        Picture.drawer("companies_by_manager_number.png")


    except Exception as e:
        print(e)


def menu():
    menu = """
---------------------------------------------------------
1. - Picture about the project statics                   )
2. - Picture about the budget statics                    )
3. - Picture about the maintenance statics.              )
4. - Picture about the Companies with the most managers. )
5. - Picture about project name by status                )
6. - Exit.                                               )
---------------------------------------------------------"""

    print(menu)

menu()
try:
    select = int(input("Pick a number:"))
except:
    print("Invalid key !")
    exit()
if select == 1:
    companies_by_project_number()
    img = Image.open('companies_by_project_number.png')
    img.show()
elif select == 2:
    projects_by_currency()
    img = Image.open('projects_by_currency.png')
    img.show()
elif select == 3:
    companies_by_maintenance()
    img = Image.open('companies_by_maintenance.png')
    img.show()
elif select == 4:
    companies_by_manager_number()
    img = Image.open('companies_by_manager_number.png')
    img.show()
elif select == 5:
    project_name_by_status()
    img = Image.open('project_name_by_status.png')
    img.show()
else:
    exit()
