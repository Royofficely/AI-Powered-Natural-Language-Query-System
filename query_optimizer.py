import json
import openai
from colorama import Fore
from utils import agent_print
from config import LLM_CONFIG

def optimize_query(prompt, schema, db_structure, context):
    agent_print("Query Optimizer", "Optimizing query...", Fore.MAGENTA)

    schema_info = "\n".join([f"Table: {row[0]}, Column: {row[1]}, Type: {row[2]}" for row in schema])
    structure_info = json.dumps(db_structure, indent=2)

    message = f"""
    Given the following database schema, structure, and recent chat history:

    Schema:
    {schema_info}

    Structure:
    {structure_info}

    Recent Chat History:
    {context}

    Optimize this user query to match the database structure and consider the chat history:
    {prompt}

    Please ensure the following:
    1. The query is case-insensitive for string comparisons.
    2. Use the LOWER() function for case-insensitive comparisons where appropriate.
    3. Take into account the relationships between tables when constructing JOINs.
    4. Be aware that some fields might be of JSON type and require special handling.
    5. Avoid using SELECT * for tables with JSON columns. Instead, list out the specific columns needed.
    6. If JSON data needs to be retrieved, use the appropriate PostgreSQL JSON functions.
    7. Consider the chat history when interpreting the user's query, especially for follow-up questions or references to previous results.
    8. For the 'users' table, use 'bs_name' (business name) or 'uphone_number' (user phone number) instead of 'name' when referring to user identifiers.
    9. Return only the optimized SQL query, without any explanations or additional text.
    """

    response = openai.ChatCompletion.create(
        model=LLM_CONFIG['model'],
        messages=[
            {"role": "system", "content": "You are a database query optimizer."},
            {"role": "user", "content": message}
        ],
        max_tokens=300
    )

    optimized_prompt = response['choices'][0]['message']['content'].strip()
    agent_print("Query Optimizer", f"Optimized query: {optimized_prompt}", Fore.MAGENTA)
    return optimized_prompt