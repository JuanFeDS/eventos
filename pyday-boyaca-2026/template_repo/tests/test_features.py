"""Pruebas de las features derivadas."""

from src.features.engineering import compute_engagement_score


def test_engagement_score_is_product_of_sessions_and_completion(sample_df):
    """engagement_score debe ser sessions_last_30d por completion_rate."""
    result = compute_engagement_score(sample_df)
    assert (result["engagement_score"] == result["sessions_last_30d"] * result["completion_rate"]).all()
