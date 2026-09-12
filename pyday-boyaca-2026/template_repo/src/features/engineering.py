"""Features derivadas del comportamiento y riesgo de los clientes de Streamly."""

RIESGO_POR_METODO_PAGO = {
    "tarjeta_credito": 0.0,
    "tarjeta_debito": 0.1,
    "pse": 0.2,
    "paypal": 0.15,
}


def compute_engagement_score(df):
    """Combina sesiones y finalización de contenido en un solo indicador de uso."""
    df["engagement_score"] = df["sessions_last_30d"] * df["completion_rate"]
    return df


def compute_payment_risk(df):
    """Combina pagos fallidos con el riesgo histórico del método de pago."""
    riesgo_metodo = df["payment_method"].map(RIESGO_POR_METODO_PAGO)
    df["payment_risk"] = df["failed_payments"] + riesgo_metodo
    return df


def compute_customer_activity(df):
    """Combina dispositivos y variedad de contenido consumido."""
    df["customer_activity"] = df["devices_used"] * df["unique_content_last_30d"]
    return df


def compute_support_intensity(df):
    """Suma tickets de soporte y reclamos en un solo indicador de fricción."""
    df["support_intensity"] = df["support_tickets"] + df["complaints"]
    return df


def add_features(df):
    """Aplica todas las features derivadas sobre el dataset de Streamly."""
    df = compute_engagement_score(df)
    df = compute_payment_risk(df)
    df = compute_customer_activity(df)
    df = compute_support_intensity(df)
    return df
