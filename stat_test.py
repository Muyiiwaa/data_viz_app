import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import google.generativeai as gen_ai
import os
from dotenv import load_dotenv
import time


# creating the AI statistics function

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

def conclude(columns, test,result, alpha=0.05):
    prompt2 =f'''
    You are an expert statistician, i need you to write detailed conclusion on this analysis.
    I need you to interprete the findings of {result} performed on {columns}. Your output must be very detailed
    and sound professional.To help bring consistency in your tone, 
    i want you to always follow this output style.
    {test} Conclusion
    1.Our Question of interest:

    2.Hypothesis:

    3. Statistical Test:

    {test} was conducted to ...

    4.Decision rule:
    if pvalue is less than alpha, we reject the null hypothesis else we accept.

    5.Results:

    6.Interpretation:

    7.Conclusion:
    
    Last piece of instruction for you, anything that is a python list you should
    not include the square bracket. 
    '''
    response = model.generate_content(prompt2)

    return response.text


def display_test(df, columns, test):
    if test.lower() == 'correlation':
        p_corr, pv = stats.pearsonr(df[columns[0]].values, df[columns[1]].values)
        k_corr, kv = stats.kendalltau(df[columns[0]].values, df[columns[1]].values)
        s_corr, sv = stats.spearmanr(df[columns[0]].values, df[columns[1]].values)
        results = [[p_corr,pv],
                [k_corr,kv],
                [s_corr, sv]]
        results = pd.DataFrame(data=results, index = ['pearson','kendal', 'spearman'],
                            columns = ['correlation coefficient', 'P Value'])
    elif test.lower() == 'chi-square':
        df_cross = pd.crosstab(df[columns[0]], df[columns[1]])
        chi_stats, pv,dof,exp = stats.chi2_contingency(df_cross)
        data = {
            'chi-square stats': [chi_stats],
            'p-value': [pv],
            'degree of freedom': [dof]
        }
        results = pd.DataFrame(data)
    elif test.lower() == 'one way-anova':
        model = ols(f'{columns[1]} ~ {columns[0]}', data=df).fit()
        results = anova_lm(model)
        pv = results['PR(>F)'].loc[columns[0]]
    elif test.lower() == "fisher's-exact":
        df_cross = pd.crosstab(df[columns[0]], df[columns[1]])
        fish_stats, pv = stats.fisher_exact(df_cross)
        data = {
            "fisher's stats": [fish_stats],
            'p-value': [pv]
        }
        results = pd.DataFrame(data)
    elif test.lower() == 'regression':
        X = sm.add_constant(df[columns[1:]])
        y = df[columns[0]]
        model = sm.OLS(y, X).fit()
        results = model.summary()
    elif test.lower() == 'mann-whitney-u':
        groups = list(df[columns[0]].unique())
        data_group1 = df[df[columns[0]] == groups[0]][columns[1]].values
        data_group2 = df[df[columns[0]] == groups[1]][columns[1]].values
        m_statistic, pv = stats.mannwhitneyu(data_group1, data_group2)
        results = pd.DataFrame([[m_statistic],[pv]], columns= ['values'],
                               index = ['test statistic', 'p value'])
    elif test.lower() == 'wilcoxon rank':
        groups = list(df[columns[0]].unique())
        data_group1 = df[df[columns[0]] == groups[0]][columns[1]].values
        data_group2 = df[df[columns[0]] == groups[1]][columns[1]].values
        w_statistic, pv = stats.wilcoxon(data_group1, data_group2)
        results = pd.DataFrame([[w_statistic],[pv]], columns= ['values'],
                               index = ['test statistic', 'p value'])
    elif test.lower() == 'kruskal-wallis':
        result = stats.kruskal(*[group[columns[1]] for name, group in df.groupby(columns[0])])
        k_statistic, pv = (result.statistic, result.pvalue)
        results = pd.DataFrame([[k_statistic],[pv]], columns= ['values'],
                               index = ['test statistic', 'p value'])
    elif test.lower() == 'two-way anova':
        model = ols(f'{columns[2]} ~ {columns[0]} + {columns[1]} + {columns[0]}:{columns[1]}', data=df).fit()
        results = anova_lm(model)
        pv_0 = results['PR(>F)'].loc[columns[0]]
        pv_1 = results['PR(>F)'].loc[columns[1]]
        pv_0_1 = results['PR(>F)'].loc[columns[0]]
    elif test.lower() == 't-test':
        groups = list(df[columns[0]].unique())
        data_group1 = df[df[columns[0]] == groups[0]][columns[1]].values
        data_group2 = df[df[columns[0]] == groups[1]][columns[1]].values
        t_statistic, pv = stats.ttest_ind(data_group1, data_group2)
        results = pd.DataFrame([[t_statistic],[pv]], columns= ['values'],
                               index = ['test statistic', 'p value'])
    with st.container(height=500):
        st.write(results)
        st.subheader('Conclusion', divider=True)
        progress_text = "Analyzing the result. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
             time.sleep(0.03)
             my_bar.progress(percent_complete + 1, text=progress_text)
        st.write(conclude(columns=columns, test=test, result = results))
