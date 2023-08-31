import seaborn as sns
import matplotlib.pyplot as plt

def line_plot(company, df, x, y):
    
    # Initializing plot with data
    lp = sns.lineplot(data=df, x=x, y=y)
    
    # Styling
    sns.set_style("darkgrid")
    sns.set_context("paper", rc={"lines.linewidth": 3})
    sns.set_theme(rc={'axes.facecolor': (0,0,0,0), 'figure.facecolor':(0,0,0,0)})

    # Annotations
    lp.set_title(f'Closing price of {company}', color='white')
    

    return lp.get_figure()

    