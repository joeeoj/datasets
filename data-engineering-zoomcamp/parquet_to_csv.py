from pathlib import Path
import sys

import pandas as pd


if __name__ == '__main__':
    fname = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('yellow_tripdata_2021-01.parquet')
    print(fname)

    df = pd.read_parquet(fname)
    df.to_csv(fname.with_suffix('.csv'), index=False)
