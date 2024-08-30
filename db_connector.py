import psycopg2
import mysql.connector
from sqlalchemy import create_engine, inspect
from config import DB_CONFIG
from utils import agent_print
from colorama import Fore

def get_db_connection():
    if DB_CONFIG['type'] == 'postgres':
        return psycopg2.connect(
            dbname=DB_CONFIG['dbname'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port']
        )
    elif DB_CONFIG['type'] == 'mysql':
        return mysql.connector.connect(
            database=DB_CONFIG['dbname'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port']
        )
    else:
        raise ValueError(f"Unsupported database type: {DB_CONFIG['type']}")

def get_db_schema():
    agent_print("DB Connector", "Connecting to the database...", Fore.CYAN)
    conn = get_db_connection()
    cursor = conn.cursor()

    agent_print("DB Connector", "Fetching schema information...", Fore.CYAN)

    if DB_CONFIG['type'] == 'postgres':
        cursor.execute("""
            SELECT table_name, column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = 'public'
            ORDER BY table_name, ordinal_position
        """)
    elif DB_CONFIG['type'] == 'mysql':
        cursor.execute("""
            SELECT table_name, column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = %s
            ORDER BY table_name, ordinal_position
        """, (DB_CONFIG['dbname'],))

    schema = cursor.fetchall()
    cursor.close()
    conn.close()

    agent_print("DB Connector", "Schema retrieved successfully!", Fore.CYAN)
    return schema

def get_db_structure():
    agent_print("DB Analyzer", "Analyzing database structure...", Fore.YELLOW)

    if DB_CONFIG['type'] == 'postgres':
        engine_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    elif DB_CONFIG['type'] == 'mysql':
        engine_url = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    
    engine = create_engine(engine_url)
    inspector = inspect(engine)

    structure = {}
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        foreign_keys = inspector.get_foreign_keys(table_name)

        structure[table_name] = {
            "columns": [{"name": col['name'], "type": str(col['type'])} for col in columns],
            "foreign_keys": foreign_keys
        }

    agent_print("DB Analyzer", "Database structure analysis complete!", Fore.YELLOW)
    return structure