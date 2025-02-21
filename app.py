import streamlit as st
import polars as pl

@st.cache_data(show_spinner=False)
def load_parquet(file_path: str) -> pl.DataFrame:
    # Lit le fichier Parquet avec Polars (idéal pour de gros fichiers grâce à son moteur optimisé en Rust)
    return pl.read_parquet(file_path)

def main():
    st.title("App Streamlit : Lecture de Parquet avec Polars")
    
    file_path = st.text_input("Chemin vers le fichier Parquet (ex: data.parquet)", "dataset_1GB.parquet")
    
    if file_path:
        with st.spinner("Chargement du fichier Parquet..."):
            df = load_parquet(file_path)
        st.success("Fichier chargé avec succès !")
        st.write("Aperçu des 10 premières lignes :")
        st.dataframe(df.head(10).to_pandas())
        st.write("Dimensions du dataset :", df.shape)

if __name__ == "__main__":
    main()
