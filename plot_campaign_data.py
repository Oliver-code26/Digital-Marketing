import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "online_advertising_performance_data.csv"
DEFAULT_OUTPUT_PATH = "jupyter_notebooks/Pie_chart_camp1.png"


def load_dataset(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the advertising performance dataset from CSV."""
    return pd.read_csv(path)


def plot_camp1_engagement_by_banner_placement(dataset: pd.DataFrame, output_path: str = DEFAULT_OUTPUT_PATH) -> None:
    """Plot a pie chart for camp 1 using banner + placement and save it."""
    camp1 = dataset[dataset["campaign_number"] == "camp 1"].copy()
    camp1["displays"] = pd.to_numeric(camp1["displays"], errors="coerce").fillna(0).astype(int)
    camp1["group"] = camp1["banner"].astype(str) + " | " + camp1["placement"].astype(str)

    summary = camp1.groupby("group")["displays"].sum().sort_values(ascending=False)
    top = summary.head(10)
    others = summary.iloc[10:].sum()
    labels = top.index.tolist()
    sizes = top.values.tolist()

    if others > 0:
        labels.append("Other")
        sizes.append(int(others))

    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, pctdistance=0.85)
    plt.title("Camp 1 engagement by banner + placement (displays)")
    centre_circle = plt.Circle((0, 0), 0.55, fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close(fig)
    print(f"Saved pie chart to {output_path}")


if __name__ == "__main__":
    df = load_dataset()
    plot_camp1_engagement_by_banner_placement(df)
