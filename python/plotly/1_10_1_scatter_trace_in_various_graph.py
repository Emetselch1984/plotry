#Various graphs
# Scatter Trace
import plotly.graph_objects as go
data1 = {
    "x": [1,2,3],
    "y": [1,5,3],
    "hovertext": ["A社","B社","C社"],
    "name": "bar"
}
scatter = go.Scatter(
    x=data1['x'],y=data1['y'],
    hovertext=data1['hovertext'],
    name=data1['name'])
fig = go.Figure()
fig.add_traces([scatter])
fig.show()
# drawing with data stocks
import plotly
stocks = plotly.data.stocks()
stocks.head()
config1 = {
    "x": stocks["date"],
    "y": stocks["GOOG"],
    "hovertext": ["A社","B社","C社"],
    "name": "stocks data",
    "title": {'text': "stocksデータ" },
    "xaxis": {
        "rangesslider": {"visible" : True},
        "rangeselector": {
            "buttons": [
                {"labels":"1m","step":"month","count":1},
                {"labels":"7d","step":"day","count":7},
                {"step":"all"}
            ]
        }
    }
}
scatter = go.Scatter(
    x=config1['x'],y=config1['y'],
    hovertext=config1['hovertext'],
    name=config1['name'])
fig = go.Figure()
fig.add_traces([scatter])
fig.layout.update(title=config1["title"])
fig.show()
# use rangeslider,rangeselector
import plotly
stocks = plotly.data.stocks()
stocks.head()
config1 = {
    "x": stocks["date"],
    "y": stocks["GOOG"],
    "hovertext": ["A社","B社","C社"],
    "name": "stocks data",
    "title": {'text': "stocksデータ" },
    "xaxis": {
        "rangeslider": {"visible" : True},
        "rangeselector": {
            "buttons": [
                {"label":"1m","step":"month","count":1},
                {"label":"7d","step":"day","count":7},
                {"step":"all"}
            ]
        }
    }
}
scatter = go.Scatter(
    x=config1['x'],y=config1['y'],
    hovertext=config1['hovertext'],
    name=config1['name'])
layout = go.Layout(
    title= config1["title"],
    xaxis= config1["xaxis"]
)
fig = go.Figure(
    scatter,
    layout= layout
)
fig.show()
