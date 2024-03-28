import plotly.express as px
import plotly.express as px
import plotly.graph_objects as go

def generate_plotly_chart(chart_type, data, cols):
    chart_functions = {
        'Scatter': px.scatter(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Bar': px.histogram(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Line': px.line(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Pie': px.pie(data, names= cols[0], values= cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Histogram': px.histogram(data, x = cols[0],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Box': px.box(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Violin': px.violin(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        #'Scatter3d': px.scatter_3d(data, x = cols[0], y = cols[1], z = cols[2],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        #'Bubble' : px.scatter(data, x=cols[0], y=cols[1],size=cols[2],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Funnel': px.funnel(data, x=cols[0], y=cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}')
    }

    if chart_type not in chart_functions:
        raise ValueError("Invalid chart type specified.")

    return chart_functions[chart_type]

chart_dict = {
    'Scatter': 'Shows the relationship between two continuous variables. Requires X and Y. e.g., Height vs Weight.',
    'Bar': 'Displays the relationship between a categorical and continuous variable. Requires X and Y. Categorical variable in X, continuous variable in Y. e.g., Country vs Sales.',
    'Line': 'Visualizes data points in a continuous sequence. Requires X and Y. e.g., Time vs Temperature.',
    'Pie': 'Illustrates the proportion of each category in a dataset. Requires labels and values. e.g., Market Share of Companies.',
    'Histogram': 'Represents the distribution of a continuous variable. Requires a single variable. e.g., Distribution of Exam Scores.',
    'Box': 'Displays the distribution of a continuous variable and identifies outliers. Requires X and Y. Categorical variable in X, continuous variable in Y. e.g., Gender vs Height.',
    'Violin': 'Similar to a box plot but provides a more detailed distribution of the data. Requires X and Y. Categorical variable in X, continuous variable in Y. e.g., Age Group vs Income.',
    'Funnel': 'Visualizes data in a matrix where colors represent values. Requires X, Y, and Z. e.g., Correlation Matrix of Variables.',
    'Bubble': 'Displays the 3D surface in 2D by representing contours. Requires X, Y, and Z. e.g., Elevation on a Terrain.',
    'Scatter3d': 'Shows the relationship between three continuous variables in a 3D space. Requires X, Y, and Z. e.g., Temperature vs Pressure vs Altitude.'
}


