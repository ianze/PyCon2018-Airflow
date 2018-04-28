import psycopg2
import sys

try:
    conn = psycopg2.connect("host=postgres dbname=airflow password=pycon user=pycon")
    conn.close()
    sys.exit(0)

except psycopg2.OperationalError as ex:
    sys.exit(1)
