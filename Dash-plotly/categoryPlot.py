import plotly.graph_objs as go
import pandas as pd

dfUkAccident = pd.read_csv('dfUKAccident.csv', nrows=1000);

listGOFunc = {
    "bar": go.Bar,
    "violin": go.Violin,
    "box": go.Box
}
def getPlot(table, jenis, xCategory) :
    return [listGOFunc[jenis](
                x=dfUkAccident[xCategory],
                y=dfUkAccident['Speed_limit'],
                # text=dfUkAccident['High_Risk'],
                opacity=0.7,
                name='Speed Limit',
                marker=dict(color='blue')
            ),
            listGOFunc[jenis](
                x=dfUkAccident[xCategory],
                y=dfUkAccident['Age_of_Driver'],
                # text=dfUkAccident['High_Risk'],
                opacity=0.7,
                name='Age',
                marker=dict(color='orange')
            )]