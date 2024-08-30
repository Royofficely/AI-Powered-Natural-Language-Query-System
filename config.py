import os
from dotenv import load_dotenv
from zoneinfo import ZoneInfo  # Python 3.9+, or use pytz for earlier versions

# Load environment variables
load_dotenv()

# Database configuration
DB_CONFIG = {
    "type": os.getenv("DB_TYPE", "postgres"),  # or "mysql"
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# LLM configuration
LLM_CONFIG = {
    "model": os.getenv("LLM_MODEL", "gpt-4o"),
    "max_tokens": int(os.getenv("LLM_MAX_TOKENS", 500)),
    "chunk_size": int(os.getenv("LLM_CHUNK_SIZE", 1000)),
    "temperature": float(os.getenv("LLM_TEMPERATURE", 0.7))
}

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# File paths
DB_CONFIG_FILE = os.getenv("DB_CONFIG_FILE", 'db_config.json')

# Logging configuration
LOG_FILE = os.getenv("LOG_FILE", 'nl_query.log')
LOG_LEVEL = os.getenv("LOG_LEVEL", 'INFO')
LOG_FORMAT = os.getenv("LOG_FORMAT", '%(asctime)s - %(levelname)s - %(message)s')

# Caching configuration
ENABLE_SCHEMA_CACHE = os.getenv("ENABLE_SCHEMA_CACHE", "True").lower() == "true"
ENABLE_DB_STRUCTURE_CACHE = os.getenv("ENABLE_DB_STRUCTURE_CACHE", "True").lower() == "true"

# Time zone configuration
TIME_ZONE = ZoneInfo(os.getenv("TIME_ZONE", "Asia/Jerusalem"))  # Default to Israel time if not specified

# Query result configuration
RESULTS_PER_PAGE = int(os.getenv("RESULTS_PER_PAGE", 10))
MAX_RESULTS = int(os.getenv("MAX_RESULTS", 1000))

# Security configuration
ENABLE_SSL = os.getenv("ENABLE_SSL", "False").lower() == "true"
SSL_CERT_PATH = os.getenv("SSL_CERT_PATH", "")
SSL_KEY_PATH = os.getenv("SSL_KEY_PATH", "")

# Performance tuning
DB_CONNECTION_POOL_SIZE = int(os.getenv("DB_CONNECTION_POOL_SIZE", 5))
QUERY_TIMEOUT = int(os.getenv("QUERY_TIMEOUT", 30))  # in seconds

# Feature flags
ENABLE_QUERY_OPTIMIZATION = os.getenv("ENABLE_QUERY_OPTIMIZATION", "True").lower() == "true"
ENABLE_CHAT_HISTORY = os.getenv("ENABLE_CHAT_HISTORY", "True").lower() == "true"

# Error handling
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", 1))  # in seconds

# Custom prompts
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are a helpful AI assistant for database queries.")
USER_PROMPT = os.getenv("USER_PROMPT", "Please provide a natural language query for the database.")

# Additional configurations can be added here as needed