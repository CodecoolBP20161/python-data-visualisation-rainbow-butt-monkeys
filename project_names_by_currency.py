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

    @staticmethod
    def make_reverse_order(project_list):
        projects = []
        all_companies = ProjectByCurrency.currency_change(project_list)

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
                now.append(round(i.budget_value / 150))
                now.append(i.main_color)
                all.append(now)

        return sorted(all, key=getKey, reverse=True)