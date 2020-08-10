import networkx as nx
import matplotlib.pyplot as plt

import plotly.graph_objects as go
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
    # os.chdir(os.getcwd() + "/pictures")

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

        pos = nx.spring_layout(graph, k=0.9, iterations=5000)
        for n, p in pos.items():
            graph.nodes[n]['pos'] = p

        edge_trace = go.Scatter(
            x=[], y=[],
            line=dict(width=4, color='#888'),
            hoverinfo='none',
            mode='lines')

        for edge in graph.edges():
            x0, y0 = graph.nodes[edge[0]]['pos']
            x1, y1 = graph.nodes[edge[1]]['pos']
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

        node_trace = go.Scatter(
            x=[], y=[],
            text=[],
            textposition="middle center",
            textfont=dict(
                color="Black",
                family="Gravitas One",
                size=15,
            ),
            mode='markers+text',
            hovertext=[],
            hoverinfo='text',
            marker=dict(
                showscale=False,
                color=["Green"],
                size=[],
                opacity=[1],
                line_width=2))

        for node in graph.nodes():
            x, y = graph.nodes[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        for node, adjacencies in enumerate(graph.adjacency()):
            node_trace['marker']['color'] += tuple(["Yellow"])
            node_info = adjacencies[0]
            node_trace['text'] += tuple([node_info])
            # node_trace['hovertext'] += tuple([])
            node_trace['marker']['opacity'] += tuple([0.8])
            node_trace['marker']['size'] += tuple([len(node_info) * 11])

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='<br>Граф компаний',
                            titlefont_size=16,
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            annotations=[dict(
                                text="Python code: <a href='https://github.com/LuckyDmitry/Fintech-Securety-Superhero/'> https://github.com/LuckyDmitry/Fintech-Securety-Superhero/</a>",
                                showarrow=False,
                                xref="paper", yref="paper",
                                x=0.005, y=-0.002)],
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )
        fig.show()


clean_company = edit_data.no_data_companies


# def clean_company_graph(clean_company):
#     if len(clean_company) > 15:
#         clean_company = edit_companies(clean_company)
#         #print(parties)
#     else:
#         clean_company = [clean_company]
#     os.chdir(os.getcwd() + "/pictures_of_clean_company")
#
#     for i in range(len(clean_company)):
#         graph = nx.Graph()
#         graph.add_node("Clean Company")
#         for company in clean_company[i]:
#             graph.add_node(company)
#             graph.add_edge("Clean Company", company)
#             fig = plt.figure(figsize=(14, 14))
#             ax = plt.subplot(111)
#             ax.set_title(user_feature, fontsize=10)
#
#             nx.draw(graph,
#                     node_size=6000,
#                     node_color="red",
#                     with_labels=True,
#                     alpha=1,
#                     width=2,
#                     font_weight=570,
#                     edge_color="grey")
#         picture_name = "graph" + str(i+1) + ".png"
#         plt.savefig(picture_name, format="PNG")


def clean_company_graph(clean_company):
    if len(clean_company) > 15:
        clean_company = edit_companies(clean_company)
        #print(parties)
    else:
        clean_company = [clean_company]
    # os.chdir(os.getcwd() + "/pictures_of_clean_company")

    for i in range(len(clean_company)):
        graph = nx.Graph()
        graph.add_node("Clean Company")
        for company in clean_company[i]:
            graph.add_node(company)
            graph.add_edge("Clean Company", company)

        pos = nx.spring_layout(graph, k=0.9, iterations=5000)
        for n, p in pos.items():
            graph.nodes[n]['pos'] = p

        edge_trace = go.Scatter(
            x=[], y=[],
            line=dict(width=4, color='#888'),
            hoverinfo='none',
            mode='lines')

        for edge in graph.edges():
            x0, y0 = graph.nodes[edge[0]]['pos']
            x1, y1 = graph.nodes[edge[1]]['pos']
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

        node_trace = go.Scatter(
            x=[], y=[],
            text=[],
            textposition="middle center",
            textfont=dict(
                color="Black",
                family="Gravitas One",
                size=15,
            ),
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
                showscale=False,
                color=["Green"],
                size=[],
                opacity=[1],
                line_width=2))

        for node in graph.nodes():
            x, y = graph.nodes[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        for node, adjacencies in enumerate(graph.adjacency()):
            node_trace['marker']['color'] += tuple(["Yellow"])
            node_info = adjacencies[0]
            node_trace['text'] += tuple([node_info])
            node_trace['marker']['opacity'] += tuple([0.8])
            node_trace['marker']['size'] += tuple([len(node_info) * 11])


        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='<br>Граф компаний',
                            titlefont_size=16,
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            annotations=[dict(
                                text="Python code: <a href='https://github.com/LuckyDmitry/Fintech-Securety-Superhero/'> https://github.com/LuckyDmitry/Fintech-Securety-Superhero/</a>",
                                showarrow=False,
                                xref="paper", yref="paper",
                                x=0.005, y=-0.002)],
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )
        fig.show()

clean_company_graph(clean_company)
graph_feature(user_feature)
