import data
import matplotlib.pyplot as plt

if __name__ == "__main__":
    frame = data.build_predictors(data.load_raw())

    #building the summary stats table
    stats = frame.agg(["mean", "std", "min", "max"]).T
    stats["first"] = frame.apply(lambda x: x.first_valid_index())
    stats["last"] = frame.apply(lambda y: y.last_valid_index())
    print(stats)
    stats.to_csv("figures/summary_stats.csv")
    stats.to_markdown("figures/summary_stats.md")

    #building time series plot of each predictor
    fig, axes = plt.subplots(5, 3, figsize = (15, 18))
    axes = axes.flatten()

    for i, col in enumerate(frame.columns):
        ax = axes[i]
        ax.plot(frame.index.to_timestamp(), frame[col])
        ax.set_title(col)
    fig.tight_layout()
    fig.savefig("figures/predictors.png", dpi=150)

