from inspect import Attribute
from turtle import width
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
