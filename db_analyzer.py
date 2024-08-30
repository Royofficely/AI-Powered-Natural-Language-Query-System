from colorama import Fore
from config import DB_CONFIG_FILE, ENABLE_SCHEMA_CACHE, ENABLE_DB_STRUCTURE_CACHE
from utils import agent_print
from db_connector import get_db_connection, get_db_schema
from db_structure import get_db_structure
from config_manager import manage_db_config
from tree_builder import create_db_tree

# Global variables for caching
_schema_cache = None
_db_structure_cache = None

def get_cached_schema():
    global _schema_cache
    if _schema_cache is None or not ENABLE_SCHEMA_CACHE:
        conn = get_db_connection()
        _schema_cache = get_db_schema(conn)
        conn.close()
    return _schema_cache

def get_cached_structure():
    global _db_structure_cache
    if _db_structure_cache is None or not ENABLE_DB_STRUCTURE_CACHE:
        _db_structure_cache = get_db_structure()
    return _db_structure_cache

def analyze_database():
    agent_print("DB Analyzer", "Starting database analysis...", Fore.GREEN)
    
    schema = get_cached_schema()
    structure = get_cached_structure()
    config = manage_db_config(DB_CONFIG_FILE, structure)
    db_tree = create_db_tree(schema)
    
    agent_print("DB Analyzer", "Database analysis completed.", Fore.GREEN)
    
    return schema, structure, config, db_tree

if __name__ == "__main__":
    analyze_database()