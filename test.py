import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML
df_data = px.data.iris()
fig = px.scatter_matrix(df_data, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")
HTML(fig.to_html())