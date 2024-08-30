from sqlalchemy import create_engine, inspect
from config import DB_CONFIG
from utils import agent_print
from colorama import Fore

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