import edit_data
import plotly.graph_objects as go


feature_company = edit_data.feature_companies

#получение отсортированных по популярности features
def get_popular() -> list:
    popularity = {}
    for feature, companies in feature_company.items():
        popularity[feature] = len(companies)

    list_items = list(popularity.items())
    list_items.sort(key=lambda i: i[1])

    return list_items

popularity = get_popular()


def draw_popular(popularity):
    colors = ["#2FA465", ] * len([popularity[i][0] for i in range(len(popularity))])
    colors[len(popularity) - 1] = 'crimson'

    fig = go.Figure(data=[go.Bar(
        x=[popularity[i][0] for i in range(len(popularity))],
        y=[popularity[i][1] for i in range(len(popularity))],
        marker_color=colors)])  # marker color can be a single color value or an iterable

    fig.update_layout(title_text='The most popular data')

    fig.show()
    return fig

draw_popular(popularity)