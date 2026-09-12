# Diccionario de columnas — streamly_churn.csv

| Columna | Tipo | Descripción |
|---|---|---|
| customer_id | string | Identificador único del cliente |
| month | date | Mes del registro (una fila por cliente/mes) |
| age | int | Edad del cliente |
| country | string | País |
| city | string | Ciudad |
| plan | string | Plan de suscripción |
| monthly_price | float | Precio mensual pagado |
| payment_method | string | Método de pago |
| subscription_months | int | Antigüedad en meses |
| sessions_last_30d | int | Sesiones en los últimos 30 días |
| hours_watched | float | Horas vistas |
| unique_content_last_30d | int | Contenido único visto en 30 días |
| completion_rate | float | Tasa de finalización de contenido |
| days_since_last_login | int | Días desde el último login |
| devices_used | int | Dispositivos usados |
| support_tickets | int | Tickets de soporte abiertos |
| complaints | int | Quejas registradas |
| failed_payments | int | Pagos fallidos |
| churn | int | Variable objetivo (1 = canceló) |
