from parser import *
from handler import Handler

if __name__ == '__main__':
    current_file = open_yaml_files()
    for entry in current_file:
        company = Handler(entry)
        company.handle_file()
        data = company.get_permissions_data()
        company_name = company.get_company_name()
        save_file(company_name, data)

