import json
import os
from datetime import datetime
from colorama import init, Fore, Style
import argparse

from config import DB_CONFIG_FILE
from db_connector import get_db_schema, get_db_structure
from query_processor import process_natural_language_query
from tree_builder import create_db_tree
from config_manager import manage_db_config

init(autoreset=True)

def get_config_creation_time():
    if os.path.exists(DB_CONFIG_FILE):
        creation_time = os.path.getctime(DB_CONFIG_FILE)
        return datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return "File not found"

def analyze_db_structure():
    print(f"{Fore.CYAN}Analyzing database structure...{Style.RESET_ALL}")
    try:
        schema = get_db_schema()
        print("Schema retrieved successfully.")

        db_structure = get_db_structure()
        print("Database structure retrieved successfully.")

        config = manage_db_config(DB_CONFIG_FILE, db_structure)
        print("Configuration managed successfully.")

        db_tree = create_db_tree(schema)
        print(f"{Fore.MAGENTA}Database Structure:{Style.RESET_ALL}")
        db_tree.show()

        print(f"\n{Fore.YELLOW}Configuration file: {DB_CONFIG_FILE}{Style.RESET_ALL}")
        print(f"Creation time: {get_config_creation_time()}")

        print(f"\n{Fore.GREEN}Analysis complete. You can now use this information for querying.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred during analysis: {str(e)}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()

def run_query_interface():
    try:
        schema = get_db_schema()
        db_structure = get_db_structure()
        with open(DB_CONFIG_FILE, 'r') as f:
            config = json.load(f)

        print(f"{Fore.CYAN}Welcome to the AI-Powered Natural Language Postgres Query System!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Type 'quit' to exit the system.{Style.RESET_ALL}")

        while True:
            user_prompt = input(f"{Fore.YELLOW}Enter your query: {Style.RESET_ALL}")
            if user_prompt.lower() == 'quit':
                break
            try:
                result = process_natural_language_query(user_prompt, schema, config, db_structure)
                print(f"{Fore.GREEN}Query Result:{Style.RESET_ALL}")
                print(result)
                print("\n")
            except Exception as e:
                print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")
                print("\n")

    except Exception as e:
        print(f"{Fore.RED}An error occurred while initializing the query interface: {str(e)}{Style.RESET_ALL}")

    print(f"{Fore.CYAN}Thank you for using the AI-Powered Natural Language Postgres Query System. Goodbye!{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Natural Language Postgres Query System")
    parser.add_argument('command', choices=['analyze', 'query'], help="Command to run: 'analyze' for database structure analysis, 'query' for running queries")

    args = parser.parse_args()

    if args.command == 'analyze':
        analyze_db_structure()
    elif args.command == 'query':
        run_query_interface()

if __name__ == "__main__":
    main()