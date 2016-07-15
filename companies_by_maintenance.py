from textbox import TextBox

class CompaneiesByMaintenance:

    def __init__(self, name, company_name, maintenance_requested, main_color):
        self.name = name
        self.company_name = company_name
        self.maintenance_requested = maintenance_requested
        self.main_color = main_color


    @staticmethod
    def output_maker(projects):
        dictionary = {}
        for row in projects:
            if row.company_name not in dictionary and row.maintenance_requested != "true":
                dictionary.setdefault(row.company_name, [])
                if row.maintenance_requested != "true":
                    dictionary[row.company_name].append(row.maintenance_requested)
                    dictionary[row.company_name].append(row.main_color)
            else:
                if row.maintenance_requested != "true":
                    dictionary.setdefault(row.company_name, []).append(row.maintenance_requested)
                    dictionary.setdefault([row.company_name].append(row.main_color))
        list = []
        for k, v in dictionary.items():
            if v != None:
                sublist = []
                dictionary[k] = v[0], TextBox.hex_to_rgb(v[1]), v[2:]
                sublist.append(k)
                sublist.append(TextBox.hex_to_rgb(v[1]))
                a = 0
                for i in v:
                    if "false" == i:
                        a += 1
                sublist.append(a*30)
                list.append(sublist)
        return list