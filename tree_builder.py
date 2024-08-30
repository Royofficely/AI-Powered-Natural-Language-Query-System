from treelib import Tree
from utils import agent_print
from colorama import Fore

def create_db_tree(schema):
    agent_print("Tree Builder", "Creating database tree structure...", Fore.MAGENTA)

    db_tree = Tree()
    db_tree.create_node("Database", "database")

    table_count = {}
    for table, column, data_type in schema:
        if table not in table_count:
            table_count[table] = 0
        else:
            table_count[table] += 1

        table_id = f"{table}_{table_count[table]}"
        if not db_tree.contains(table_id):
            db_tree.create_node(table, table_id, parent="database")

        column_id = f"{table}_{column}"
        column_data = f"{column} ({data_type})"
        db_tree.create_node(column_data, column_id, parent=table_id)

    agent_print("Tree Builder", "Database tree structure created!", Fore.MAGENTA)
    return db_tree