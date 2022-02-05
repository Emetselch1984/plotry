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