from inspect import Attribute
from turtle import width
from unicodedata import name
import plotly.graph_objects as go
fig = go.Figure()
fig.show()

# traceによるグラフ登録
# About Trace 
# register a graph

scatter_trace = go.Scatter(x=[1,2,3],y=[3,1,6])
scatter_fig = go.Figure(data=scatter_trace)
scatter_fig.show()

data = {
    'x': [1,2,3],
    'y': [4,3,1]
}
bar_tarace = go.Bar(x=data['x'],y=data['y'])
scatter_bar_fig = go.Figure(data=[scatter_trace,bar_tarace])
scatter_bar_fig.show()

# traceによるグラフ登録
# About Layout 
# adjusts a graph
data = {
    'width': 300,
    'height': 300
}
layout = go.Layout(width= data['width'],height = data['height'])
fix_size_fig = go.Figure(data=scatter_trace,layout = layout)
fix_size_fig.show()

# plotly.jsのデータ構造
# data structure
fig.to_json()[:80]
fig.to_json()[80:]
fig.to_json()[:]
# 属性の設定方法
# How to set up attribute
# set attribute
import plotly.graph_objects as go
title = {'text': "グラフタイトル" }
layout = go.Layout(title=title)
fig = go.Figure(layout=layout)
fig.show()
# 属性の変更
# update attribute
title = {'text': "グラフタイトル改" }
fig.layout.update(title=title)
fig.show()
title = {'text': "グラフタイトル改弐" }
fig.update_layout(title=title)
fig.show()
# add attribute
data1 = {
    "x": [1,2,3],
    "y": [1,5,3]
}
scatter = go.Scatter(x=data1['x'],y=data1['y'])
fig2 = go.Figure()
fig2.add_trace(scatter)
data2 = {
    "x": [1,2,3],
    "y": [1,2,3]
}
bar = go.Bar(x=data2['x'],y=data2['y'])
fig2.add_trace(bar)
fig2.show()
# Method add_traces
fig3 = go.Figure()
fig3.add_traces([scatter,bar])
fig3.show()

# Interactive operation
# インタラクティブな操作
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
data2 = {
    "x": [1,2,3],
    "y": [1,2,3],
    "name": "line"
}
bar = go.Bar(x=data2['x'],y=data2['y'],name=data2['name'])
fig3 = go.Figure()
fig3.add_traces([scatter,bar])
fig3.show()

# selection attribute
import numpy
import plotly.graph_objects as go
numpy.random.seed(1)
data1 = numpy.random.randn(200,200)
data2 = numpy.random.randn(200,200)+1
config1 = {
    "x": data1[0],
    "y": data1[1],
    "name": "A",
    "mode": "markers" 
}
config2 = {
    "x": data2[0],
    "y": data2[1],
    "name": "B",
    "mode": "markers" 
}
scatter_a = go.Scatter(
    x=config1["x"],
    y=config1["y"],
    name=config1["name"],
    mode=config1["mode"])
scatter_b = go.Scatter(
    x=config2["x"],
    y=config2["y"],
    name=config2["name"],
    mode=config2["mode"])
fig = go.Figure()
fig.add_traces([scatter_a,scatter_b])
fig.show()
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

# Scatter Trace in Various graphs
# base graph
# drawing with data stocks
# use rangeslider,rangeselector

# Data containing missing values
import plotly.graph_objects as go
import numpy 
line_x_not_null = numpy.arange(5)
line_y_with_null = numpy.array([1,2,numpy.nan,4,5])
with_null_fig = go.Figure()
config1 = {
    "x": line_x_not_null,
    "y": line_y_with_null,
    "name": "default",
    "title": {'text': "欠損値を含むデーター"},
}
scatter1 = go.Scatter(
    x=config1["x"],
    y=config1["y"],
    name=config1["name"],
)
with_null_fig.add_trace(scatter1)
with_null_fig.update_layout(title=config1["title"])
# Data ignoring missing values
config2 = {
    "x": line_x_not_null,
    "y": line_y_with_null + 1,
    "name": "connectgaps",
    "connectgaps": True 
}
scatter2 = go.Scatter(
    x=config2["x"],
    y=config2["y"],
    name=config2["name"],
    connectgaps = config2["connectgaps"]
)
with_null_fig.add_trace(scatter2)
with_null_fig.show()


