import edit_data

norm_features = edit_data.new_features

#выбор компании
def choose_company():
    companies = edit_data.names_of_files

    us_company = input("Выберите компанию, о которой хотите узнать подробнее {}".format("\n".join(companies)))
    return us_company

user_company = choose_company()

#получение данных, которые отправляет компания
def get_info(user_company:str) -> list:
    company_features = edit_data.company_features

    company_info = list(company_features[user_company])

    for feature_id in range(len(company_info)):
        company_info[feature_id] = norm_features[company_info[feature_id]]

    return company_info

company_info = get_info(user_company)

#выдача информации
def give_info(user_company, company_info) -> str:
    if company_info == []:
        message = "Company {} does not correspond your personal info to any third companies".format(user_company)
    else:
        message = "Company {} gives these types of your personal info \n{}".format(user_company, "\n".join(company_info))
    print(message)
    return message

give_info(user_company, company_info)


get_info(user_company)



