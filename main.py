import os
import argparse
import pandas as pd
from src.plot_utils import plot_option_volume_area


def main():
    parser = argparse.ArgumentParser(description="Plot net option volume by strike.")
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the CSV file containing option data",
    )
    parser.add_argument(
        "--expiration",
        type=str,
        required=False,
        help="Optional expiration filter (e.g., '250505')",
    )
    args = parser.parse_args()

    # Resolve absolute path
    csv_path = os.path.abspath(args.file)

    # Load and plot
    df = pd.read_csv(csv_path)
    plot_option_volume_area(df, expiration=args.expiration)


if __name__ == "__main__":
    main()
