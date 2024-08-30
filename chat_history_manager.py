class ChatHistoryManager:
    def __init__(self, max_history=10):
        self.history = []
        self.max_history = max_history

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]

    def get_context(self):
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.history])

    def clear_history(self):
        self.history = []