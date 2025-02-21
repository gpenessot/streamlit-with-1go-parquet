import numpy as np
import polars as pl

def generate_dataset(n_rows: int, n_cols: int) -> pl.DataFrame:
    # Génère un array de float64 aléatoires
    data = np.random.rand(n_rows, n_cols)
    # Crée des noms de colonnes : col_0, col_1, ..., col_{n_cols-1}
    columns = [f"col_{i}" for i in range(n_cols)]
    return pl.DataFrame(data, schema=columns)

def main():
    # Pour obtenir environ 1 Go : 12,500,000 lignes x 10 colonnes x 8 bytes (float64) ≈ 1 Go
    n_rows, n_cols = 12_500_000, 10
    df = generate_dataset(n_rows, n_cols)
    # Sauvegarde en Parquet sans compression pour préserver la taille
    output_file = "dataset_1GB.parquet"
    df.write_parquet(output_file, compression="uncompressed")
    print(f"Dataset généré et sauvegardé dans {output_file}")

if __name__ == "__main__":
    main()
