# plotlyとは何か
## plotyly.pyとは
Ploty社が開発したインタラクティブな可視化を実現するPythonライブラリ \
plotly.pyはplotly.jsのラッパーです。plotly.jsには最終的にJSON形式のデータ構造が渡されます。 \ 
PythonからはJSON形式のデータを意識することなく扱えます。
## plotly.pyのコンセプト
1. 描写領域であるfigureの作成
2. グラフの実態であるtraceをfigureに登録
3. スタイルなどの情報を持ったlayoutによるグラフの調整
