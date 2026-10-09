
# Financial Crime Screening Pipeline
A backend data pipeline for automated sanctions screening utilizing Python and Unix shell scripting.

## Features
* Secure data ingestion and validation via Unix shell scripting.
* Rule-based fuzzy matching engine using `rapidfuzz`.
* Normalized SQLite schema with an immutable audit log for compliance.

## Setup
1. `pip install -r requirements.txt`
2. `sqlite3 aml_database.db < sql/setup_db.sql`
3. `cd scripts && bash secure_ingest.sh`