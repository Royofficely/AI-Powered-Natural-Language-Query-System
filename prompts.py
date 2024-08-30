SYSTEM_PROMPT = """
You are an AI that helps generate SQL queries based on the database schema and configuration provided below.

Schema Information:
{schema_info}

Configuration Information:
{config_info}

Structure Information:
{structure_info}
"""

USER_PROMPT = "Create an SQL query to achieve the following: {prompt}"

REFINE_PROMPT = "Refine the following SQL queries to make a single optimized query: {combined_query}"

OPTIMIZATION_PROMPT = """
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

CLARIFICATION_PROMPT = """
Given the following database schema and structure:

Schema:
{schema_info}

Structure:
{structure_info}

And the user's query:
{prompt}

Please suggest 3 possible interpretations of what the user might be asking for, based on the available data.
Each interpretation should be a full, executable SQL query.
Format your response as a numbered list, with each item starting with the number, followed by a period and a space.
"""

SHORT_QUERY_PROMPT = """
Given the short query: "{prompt}"
And the following database schema:
{db_structure}

Please provide 3 possible interpretations of what the user might be asking for, based on the available data.
Each interpretation should be a full, executable SQL query.
Format your response as a numbered list, with each item starting with the number, followed by a period and a space.
"""


TABLE_DESCRIPTION_PROMPT = """Provide a brief description for a database table named '{item_name}'. Explain its purpose and role in the database. Also, suggest 2-3 alternative names or phrases that users might use to refer to this table in natural language queries."""

COLUMN_DESCRIPTION_PROMPT = """Provide a brief description for a database column named '{item_name}' with data type '{data_type}'. Explain what information this column likely stores. Also, suggest 2-3 alternative names or phrases that users might use to refer to this column in natural language queries."""

DESCRIPTION_SYSTEM_PROMPT = """You are a helpful assistant that provides concise descriptions for database tables and columns."""