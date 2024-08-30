import pandas as pd
from sqlalchemy import create_engine, text
from colorama import Fore
from utils import agent_print
from config import DB_CONFIG, TIME_ZONE
from datetime import datetime, timedelta

def execute_query(query):
    agent_print("Query Executor", "Executing SQL query...", Fore.BLUE)

    if query is None:
        return "No valid SQL query found in the generated text."

    try:
        if DB_CONFIG['type'] == 'postgres':
            engine_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
        elif DB_CONFIG['type'] == 'mysql':
            engine_url = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
        else:
            raise ValueError(f"Unsupported database type: {DB_CONFIG['type']}")

        agent_print("Query Executor", f"Connecting to: {engine_url}", Fore.BLUE)
        engine = create_engine(engine_url)

        with engine.connect() as connection:
            agent_print("Query Executor", "Connected successfully", Fore.BLUE)
            
            # Set the timezone for the database session
            if DB_CONFIG['type'] == 'postgres':
                connection.execute(text(f"SET TIME ZONE '{TIME_ZONE}'"))
            elif DB_CONFIG['type'] == 'mysql':
                connection.execute(text(f"SET time_zone = '{TIME_ZONE}'"))
            
            sql = text(query)
            result = pd.read_sql(sql, connection)

        agent_print("Query Executor", "Query executed successfully!", Fore.BLUE)
        
        # Convert timestamp columns to the correct time zone
        for column in result.select_dtypes(include=['datetime64', 'datetime64[ns]']).columns:
            result[column] = result[column].dt.tz_localize('UTC').dt.tz_convert(TIME_ZONE)

        # Add a new column for numbering, starting from 1
        if not result.empty:
            result.insert(0, 'Row', range(1, len(result) + 1))
        
        # Print current time in the specified time zone for verification
        current_time = datetime.now(TIME_ZONE)
        agent_print("Query Executor", f"Current time in {TIME_ZONE}: {current_time}", Fore.BLUE)

        return result
    except Exception as e:
        error_msg = f"Error executing query: {str(e)}"
        agent_print("Query Executor", error_msg, Fore.RED)
        return error_msg