import psycopg2

try:
    # setup connection string
    connect_str = "dbname='svindler' user='svindler' host='localhost' password='codecool'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # removing the test table if it already exists
    cursor.execute("""SELECT name, budget_value, budget_currency, main_color FROM project;""")
    rows = cursor.fetchall()

    all_companies = []
    for row in rows:
        if row[0] not in all_companies:
            company = []
            company.append(row[0])
            company.append(float(row[1]))
            company.append(row[2])
            company.append(row[3])
            all_companies.append(company)
        else:
            pass

except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


class ProjectByCurrency:
    def __init__(self, name, budget_value, budget_currency, main_color):
        self.name = name
        self.budget_value = budget_value
        self.budget_currency = budget_currency
        self.main_color = main_color


    @staticmethod
    def currency_change(projects):
        for i in projects:
            if i[0] != None:
                if i[2] == "USD":
                    i[1] = i[1] / 1.4
                    i[2] = "EUR"
                if i[2] == "GBP":
                    i[1] = i[1] * 0.8
                    i[2] = "EUR"
            elif i[0] == None:
                pass
        return projects

projects = []
all_companies = ProjectByCurrency.currency_change(all_companies)


def getKey(item):
    return (item[1])


for i in all_companies:
    project = ProjectByCurrency(i[0], i[1], i[2], i[3])
    projects.append(project)
all = []
for i in projects:
    now = []
    if i.name != None:
        now.append(i.name)
        now.append(round(i.budget_value))
        now.append(i.main_color)
        all.append(now)

print(sorted(all, key=getKey, reverse=True))