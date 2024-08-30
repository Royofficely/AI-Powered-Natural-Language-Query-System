# 🤖💬 AI-Powered Natural Language Query System



<p align="center">
  <strong>Query your database using natural language, powered by cutting-edge AI technology.</strong>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#demo">Demo</a> •
  <a href="#quick-start-guide">Quick Start Guide</a> •
  <a href="#detailed-usage">Detailed Usage</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://wiki.postgresql.org/images/a/a4/PostgreSQL_logo.3colors.svg" alt="PostgreSQL Logo" width="100"/>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/768px-ChatGPT_logo.svg.png" alt="GPT Logo" width="100"/>
  <img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" alt="MySQL Logo" width="150"/>
</p>

## 🌟 Key Features

- 📊 **Intelligent Database Analysis**: Automatically analyze and understand your database structure.
- 💬 **Natural Language Queries**: Ask questions in plain English and get accurate results.
- 🧠 **AI-Powered Optimization**: Leverage advanced AI to optimize your queries for best performance.
- 🔄 **Automatic SQL Generation**: Convert natural language to efficient SQL queries behind the scenes.
- 🎨 **Rich, Informative Output**: Get clear, colorful, and detailed responses in your console.
- 🔌 **Multi-Database Support**: Works seamlessly with both PostgreSQL and MySQL databases.
- 🛡️ **Error Handling & Clarifications**: Smart error detection with an interactive clarification process.

## 🎥 Demo

<p align="center">
  <img src="https://officelyfiles.s3.eu-west-1.amazonaws.com/5146fca5-777b-4e99-907f-b19a3cf1b884.gif" alt="Demo GIF" width="600"/>
</p>

Watch our system in action! See how easy it is to query complex databases using simple, natural language.

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.8+
- PostgreSQL or MySQL database
- OpenAI API key

### Setup in 4 Easy Steps

1. **Clone and Navigate**
   ```bash
   git clone https://github.com/yourusername/nl-query-system.git
   cd nl-query-system
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure**
   Create a `config.py` file:
   ```python
   DB_CONFIG = {
       "type": "postgres",  # or "mysql"
       "dbname": "your_db_name",
       "user": "your_username",
       "password": "your_password",
       "host": "your_host",
       "port": "your_port"
   }
   OPENAI_API_KEY = "your_openai_api_key"
   ```

## 📘 Detailed Usage

### Analyzing Your Database

```bash
python nl_query_system.py analyze
```
This command will:
- Connect to your database (PostgreSQL or MySQL)
- Analyze its structure
- Generate a visual representation of your schema
- Save the analysis for optimizing future queries

### Querying Your Database

```bash
python nl_query_system.py query
```
Once in the query interface:
1. Type your question in natural language
2. The system will generate and execute an SQL query
3. View the results directly in your console

Example queries:
- "Show me all users who signed up in the last month"
- "What's the total revenue from each product category?"
- "List the top 5 customers by order value"
- "How many transactions were processed daily over the past week?"

## ⚙️ Configuration

Fine-tune your experience by adjusting these parameters in `config.py`:

- `LLM_CONFIG`: Customize the AI model settings
- `ENABLE_SCHEMA_CACHE`: Toggle schema caching for faster startup
- `LOG_LEVEL`: Set the desired logging detail level

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Check out our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for their groundbreaking language models
- The PostgreSQL and MySQL teams for their robust database systems
- All our contributors and supporters who make this project possible

---

<p align="center">
  Made with ❤️ by RoyNativ @OfficelyAI
</p>

<p align="center">
  <a href="https://github.com/yourusername/nl-query-system/issues">Report Bug</a> •
  <a href="https://github.com/yourusername/nl-query-system/issues">Request Feature</a>
</p>
