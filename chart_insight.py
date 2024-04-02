import plotly.express as px
import plotly.express as px
import plotly.graph_objects as go

def generate_plotly_chart(chart_type, data, cols):
    chart_functions = {
        'Scatter': px.scatter(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Bar': px.histogram(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}',color=cols[0]),
        'Line': px.line(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Pie': px.pie(data, names= cols[0], values= cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}'),
        'Histogram': px.histogram(data, x = cols[0],title=f'{chart_type} Chart of {cols[0]} ',color=cols[0]),
        'Box': px.box(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}',color=cols[0]),
        'Violin': px.violin(data, x = cols[0], y = cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}',color=cols[0]),
        #'Scatter3d': px.scatter_3d(data, x = cols[0], y = cols[1], z = cols[2],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}',color=cols[0]),
        #'Bubble' : px.scatter(data, x=cols[0], y=cols[1],size=cols[2],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}',color=cols[0]),
        'Funnel': px.funnel(data, x=cols[0], y=cols[1],title=f'{chart_type} Chart of {cols[0]} vs {cols[1]}',color=cols[0])
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

test_dict = {
    'T-Test': 'A statistical test used to compare the means of two groups. Assumes equal variances and normal distributions. e.g., Comparing means of male and female students.',
    'One Way-ANOVA': 'A statistical test used to compare the means of more than two groups. Assumes equal variances and normal distributions. e.g., Comparing means of different age groups.',
    'Chi-Square': 'A statistical test used to analyze the association between two categorical variables. No assumptions required. e.g., Analyzing the relationship between gender and smoking habits.',
    'Fisher\'s Exact': 'A statistical test used to analyze the association between two categorical variables. No assumptions required. e.g., Testing the independence of two events.',
    'Correlation': 'A statistical measure of the strength and direction of the linear relationship between two continuous variables. No assumptions required. e.g., Investigating the correlation between height and weight.',
    'Regression': 'A statistical method for modeling the relationship between a dependent variable and one or more independent variables. Assumes linearity and normality. e.g., Predicting sales based on advertising budget and product price.',
    'Mann-Whitney-U': 'A non-parametric alternative to the t-Test for comparing the medians of two groups. No assumptions required. e.g., Comparing medians of male and female students.',
    #'Wilcoxon Rank': 'A non-parametric alternative to the t-Test for comparing the medians of two groups. No assumptions required. e.g., Testing the difference between two groups without assuming normality.',
    'Kruskal-Wallis': 'A non-parametric statistical test used to compare the median of two or more groups. No assumptions required. e.g., Comparing medians of different age groups.',
    #'z-Test': 'A statistical test used to compare the means of two groups. To determine whether two groups differ or if a procedure or treatment affects the population of interest, it is frequently used in hypothesis testing. Assumes equal variances and normal distributions. e.g., Comparing means of male and female students.',
    #'F-Test': 'A statistical test used to determine whether there are significant differences between two variance estimates. Assumes normality and independence of observations. e.g., Testing for equality of variances in two groups.',
    'Two-way ANOVA': 'A statistical method used to analyze the effect of two categorical variables on a continuous variable. Assumes normality, homogeneity of variance, and independence of observations. e.g., Investigating the effects of gender and age on sales performance.',
    #'ANOVA (Repeated Measures)': 'A statistical test used to compare the means of more than two groups while accounting for repeated measures. Assumes sphericity. e.g., Comparing means of different treatments within subjects.'
}


