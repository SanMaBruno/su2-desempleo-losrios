import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, x, y, hue=None, title=""):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=x, y=y, hue=hue)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()