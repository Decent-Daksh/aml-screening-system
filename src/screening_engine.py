import pandas as pd
import sqlite3
from rapidfuzz import fuzz
import logging

logging.basicConfig(filename='screening.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_screening():
    try:
        conn = sqlite3.connect('../aml_database.db')
        cursor = conn.cursor()
        
        customers = pd.read_csv('../data/incoming_customers.csv')
        watchlist = pd.read_csv('../data/sanctions_watchlist.csv')
        
        logging.info(f"Loaded {len(customers)} customers for screening.")
        
        for _, cust in customers.iterrows():
            for _, bad_actor in watchlist.iterrows():
                score = fuzz.ratio(cust['full_name'].lower(), bad_actor['entity_name'].lower())
                if score > 85:
                    logging.warning(f"ALERT: Match found for {cust['full_name']} (Score: {score})")
                    cursor.execute("""
                        INSERT INTO Screening_Alerts (customer_id, matched_entity_id, match_score)
                        VALUES (?, ?, ?)
                    """, (cust['customer_id'], bad_actor['entity_id'], score))
        
        conn.commit()
        logging.info("Screening batch completed successfully.")
        
    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_screening()