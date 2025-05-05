import pandas as pd
import matplotlib.pyplot as plt


def plot_option_volume_area(df, expiration=None):
    # Filter out rows with missing critical data
    df = df.dropna(subset=["strike", "opt_kind", "totvolume"])

    # Optional: filter by expiration
    if expiration:
        df = df[df["exp"] == expiration]

    # Group by strike and opt_kind to get net volume
    grouped = (
        df.groupby(["strike", "opt_kind"])["totvolume"]
        .sum()
        .unstack(fill_value=0)
        .rename(columns={"call": "Net Calls", "put": "Net Puts"})
        .sort_index()
    )

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))

    # Fill between 0 and Net Calls
    ax.fill_between(
        grouped.index,
        0,
        grouped["Net Calls"],
        color="gold",
        alpha=0.6,
        label="Net Calls",
    )

    # Fill between 0 and Net Puts
    ax.fill_between(
        grouped.index,
        0,
        grouped["Net Puts"],
        color="skyblue",
        alpha=0.6,
        label="Net Puts",
    )

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Strike")
    ax.set_ylabel("Net Option Volume")
    ax.set_title(
        f"Net Call and Put Volume by Strike{f' (Exp: {expiration})' if expiration else ''}"
    )
    ax.legend()
    plt.tight_layout()
    plt.show()

    # Cumulative Delta line on a secondary axis
    # ax2 = ax1.twinx()
    # ax2.plot(
    #     df["strike"],
    #     df["cumdelta"],
    #     color="red",
    #     marker="o",
    #     linewidth=2,
    #     label="Cumulative Delta",
    # )
    # ax2.set_ylabel("Cumulative Delta")
    # ax2.legend(loc="upper right")
