# Deep-Researcher-Agent

An autonomous AI agent built in Python designed to perform deep, multi-step research on complex topics. This agent can retrieve information, synthesize data from multiple sources, and generate structured, comprehensive reports.

## ✨ Features

* **Autonomous Research:** Executes multi-step reasoning to break down complex queries.
* **Intelligent Synthesis:** Summarizes massive amounts of text into actionable insights.
* **Source Tracking:** Keeps track of citations and references used in the research process.
* **Flexible Architecture:** Easy to integrate with various LLMs (local or cloud-based).

## 🛠️ Prerequisites

Before running this project, ensure you have the following installed:
* **Python 3.9+**
* *(Optional)* **Docker** (If you prefer running this in a containerized environment)

## 🚀 Installation

**1. Navigate to the Project Directory**
Open your terminal and ensure you are inside the project folder:
```bash
cd path/to/Deep-Researcher-Agent
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install -r requirements.txt


# Example .env file
OPENAI_API_KEY=your_api_key_here
# OLLAMA_HOST=http://localhost:11434  # Uncomment if using a local open-source model

Run the main agent script from your terminal:
python main.py


Deep-Researcher-Agent/
├── main.py              # Entry point for the agent
├── agent/               # Core agent logic and prompts
├── tools/               # Custom tools the agent uses (web search, scrapers)
├── requirements.txt     # Python dependencies
└── .env.example         # Template for environment variables
