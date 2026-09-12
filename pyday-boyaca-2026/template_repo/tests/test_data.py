"""Pruebas de carga y limpieza de datos."""

from src.data.loader import clean_data


def test_clean_data_drops_missing_price(sample_df):
    """La limpieza debe eliminar filas sin precio mensual."""
    result = clean_data(sample_df)
    assert result["monthly_price"].isna().sum() == 0
