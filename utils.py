from colorama import Style

def agent_print(agent_name, message, color):
    print(f"{color}[Agent {agent_name}]: {message}{Style.RESET_ALL}")

def chunk_data(data, chunk_size=1000):
    """Split data into chunks to avoid token limits"""
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]