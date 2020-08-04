import os
import json
import matplotlib.pyplot as plt
new_features = {'Identifier_Cookie_or_similar_Tech_3rdParty': "Cookie or web-beacon files",
                'Demographic_3rdParty': "Your demographic group",
                'Contact_E_Mail_Address_3rdParty': "Email address",
                'Identifier_IP_Address_3rdParty': "IP Address",
                'Contact_City_3rdParty': "Your city or hometown",
                'Location_3rdParty': "Your location",
                'Identifier_Device_ID_3rdParty': "You device id",
                'Identifier_3rdParty': "Your unique identity",
                'Identifier_Ad_ID_3rdParty': "Your advertisment id",
                'Contact_3rdParty': "Your contact info",
                'Demographic_Age_3rdParty': "Your age",
                'Contact_Postal_Address_3rdParty':"Physical, home, work addresses",
                'Contact_Phone_Number_3rdParty':"Your phone number",
                'Contact_Address_Book_3rdParty': "Your phone book",
                'Contact_ZIP_3rdParty': "Your area code",
                'Contact_Password_3rdParty':"You credential and passwords"
               }

def list_of_files():
    directory = os.getcwd() + "\\files"
    files = os.listdir(directory)
    json_files = list(filter(lambda x: x.endswith('.json'), files))
    files = [file[:-5] for file in json_files]
    return json_files, files


companies_names, names_of_files = list_of_files()


def get_features(file_name):
    # поменяем директорию, если не находимся в папке с файлами о данных
    directory = os.getcwd()
    if not directory.endswith("files"):
        os.chdir(os.getcwd() + "\\files")

    with open(file_name) as file:
        info_data = json.load(file)
        if info_data != 0:
            features = [info_data[i][1] for i in range(len(info_data) - 1)]
            return set(features)


file_features = {}


def dict_file_features():
    for name in names_of_files:
        file_features[name] = get_features(name + ".json")
    return file_features


file_feature = dict_file_features()


def dict_feature_companies():
    features = []
    for company, data in file_feature.items():
        for feature in data:
            if feature not in features:
                features.append(feature)

    feature_company = {feature: [] for feature in features}

    for company, data in file_feature.items():
        for feature in data:
            feature_company[feature].append(company)
    return feature_company


feature_company = dict_feature_companies()

feature_company_ = {}
for key in new_features.keys():
    feature_company_[new_features[key]] = feature_company[key]


import networkx as nx

graph = nx.Graph()


graph.add_node('Your location')
for company in list(feature_company_['Your location']):
    graph.add_node(company)
    graph.add_edge('Your location', company)

fig = plt.figure(figsize=(12, 12))
ax = plt.subplot(111)
ax.set_title('Your location', fontsize=10)

nx.draw(graph,
        node_size=6000,
        node_color="#FEDC56",
        with_labels=True,
        alpha=1,
        width=1.5,
        font_weight=570,
        vmax=10000,
        edge_color="grey")

plt.savefig("graph.png", format="PNG")