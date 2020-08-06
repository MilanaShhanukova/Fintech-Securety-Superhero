import networkx as nx
import matplotlib.pyplot as plt
import os
import edit_data


feature_companies = edit_data.feature_companies


def choose_feature() -> str:
    all_features = list(feature_companies.keys())

    feature = input("Выберите любой вид информации из доступных {}".format("\n".join(all_features)))
    return feature


user_feature = choose_feature()

non_edit = []

def edit_companies(list_companies: list) :
    length = len(list_companies)

    if (length - 15) <= 15: #если маленькое число от 16 до 30
        split_point = length // 2
        non_edit.extend([list_companies[:split_point], list_companies[split_point:]])
        print(non_edit)
        return non_edit
    else:
        non_edit.append(list_companies[:15])
        list_companies = list_companies[15:]
        edit_companies(list_companies)
        return non_edit



def graph_feature(user_feature):
    os.chdir(os.getcwd() +"\.." + "\\pictures")

    companies = list(feature_companies[user_feature])

    if len(companies) > 15:
        parties = edit_companies(companies)
        print(parties)
    else:
        parties = [companies]

    for i in range(len(parties)):
        graph = nx.Graph()
        graph.add_node(user_feature)

        for company in parties[i]:
            graph.add_node(company)
            graph.add_edge(user_feature, company)

            fig = plt.figure(figsize=(14, 14))
            ax = plt.subplot(111)
            ax.set_title(user_feature, fontsize=10)

            nx.draw(graph,
                    node_size=6000,
                    node_color="#FEDC56",
                    with_labels=True,
                    alpha=1,
                    width=1.5,
                    font_weight=570,
                    edge_color="grey")
            picture_name = "graph" + str(i) + ".png"
            plt.savefig(picture_name, format="PNG")


clean_company = edit_data.no_data_companies

def clean_company_graph(clean_company):
    if len(clean_company) > 15:
        clean_company = edit_companies(clean_company)
        #print(parties)
    else:
        clean_company = [clean_company]
    os.chdir(os.getcwd() + "\.." + "\\pictures_of_clean_company")

    for i in range (len(clean_company)):
        graph = nx.Graph()
        graph.add_node("Clean Company")
        for company in clean_company[i]:
            graph.add_node(company)
            graph.add_edge("Clean Company", company)
            fig = plt.figure(figsize=(14, 14))
            ax = plt.subplot(111)
            ax.set_title(user_feature, fontsize=10)

            nx.draw(graph,
                    node_size=6000,
                    node_color="red",
                    with_labels=True,
                    alpha=1,
                    width=2,
                    font_weight=570,
                    edge_color="grey")
        picture_name = "graph" + str(i+1)+ ".png"
        plt.savefig(picture_name, format="PNG")



clean_company_graph(clean_company)
graph_feature(user_feature)