CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    account_balance DECIMAL(10,2)
);

CREATE TABLE Watchlist (
    entity_id INTEGER PRIMARY KEY,
    entity_name TEXT NOT NULL,
    risk_level TEXT
);

CREATE TABLE Screening_Alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    matched_entity_id INTEGER,
    match_score DECIMAL(5,2),
    screened_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY(matched_entity_id) REFERENCES Watchlist(entity_id)
);