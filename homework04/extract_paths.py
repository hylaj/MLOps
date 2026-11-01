from pathlib import Path

import polars as pl

ABO_ROOT = Path("data/abo/images")


def get_image_paths() -> list[str]:
    df = (
        pl.read_csv(ABO_ROOT / "metadata" / "images.csv.gz")
        .filter((pl.col("width") >= 1000) & (pl.col("height") >= 1000))
        .drop_nulls("path")
        .sample(fraction=1.0, shuffle=True, seed=42)
    )
    paths = (ABO_ROOT / "small" / p for p in df["path"])
    return [str(p) for p in paths if p.exists()]


if __name__ == "__main__":
    paths = get_image_paths()
    print(len(paths), paths[:3])
