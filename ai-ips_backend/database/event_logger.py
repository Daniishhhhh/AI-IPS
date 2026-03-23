from database.db import get_connection


def log_event(attack_type, confidence, action, latency):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO security_events
        (attack_type, confidence, recommended_action, total_latency_ms)
        VALUES (?, ?, ?, ?)
    """, (attack_type, confidence, action, latency))

    conn.commit()
    conn.close()