import psycopg2
from config import settings


def main():
    conn = psycopg2.connect(
        host=settings.db.host,
        database=settings.db.database,
        user=settings.db.user,
        password=settings.db.password,
        port=settings.db.port
    )
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM weather")
    rows = cur.fetchall()
    print(rows)
    
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
