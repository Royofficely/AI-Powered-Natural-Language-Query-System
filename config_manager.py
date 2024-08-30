import json
from utils import agent_print
from colorama import Fore
from description_generator import generate_description

def manage_db_config(db_config_file, structure):
    """Generate and manage the database configuration file with automatic descriptions"""
    agent_print("Config Manager", "Managing database configuration...", Fore.YELLOW)

    config = {}
    for table_name, table_info in structure.items():
        if table_name not in config:
            table_description = generate_description(table_name, "table")
            config[table_name] = {
                "description": table_description,
                "columns": {},
                "relationships": [fk['referred_table'] for fk in table_info['foreign_keys']]
            }

        for column in table_info['columns']:
            column_name = column['name']
            data_type = column['type']
            if column_name not in config[table_name]['columns']:
                column_description = generate_description(column_name, "column", data_type)
                config[table_name]['columns'][column_name] = {
                    "description": column_description,
                    "type": str(data_type)
                }

    # Save the updated config
    with open(db_config_file, 'w') as f:
        json.dump(config, f, indent=2)

    agent_print("Config Manager", f"Configuration file updated: {db_config_file}", Fore.YELLOW)
    return config