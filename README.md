# 🤖 YouTube Research & Blog Writer using CrewAI

An intelligent multi-agent system that researches YouTube videos and creates professional blog posts on any topic using CrewAI framework and Google Gemini AI.

## ✨ Features

- **Multi-Agent System**: Specialized AI agents for research and writing
- **YouTube Integration**: Searches and analyzes YouTube content for research
- **Google Gemini AI**: Powered by advanced language model
- **Flexible Topics**: Generate blogs on any subject
- **Professional Output**: Well-structured, engaging blog posts in Markdown format
- **Easy Setup**: Simple configuration and execution

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  User Input     │───▶│ Blog Researcher │───▶│  Blog Writer    │
│  (Any Topic)    │    │   Agent         │    │    Agent        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                               │                        │
                               ▼                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │ YouTube Tools   │    │ Professional    │
                       │ • Video Search  │    │ Blog Post       │
                       │ • Channel Search│    │ (Markdown)      │
                       └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/sujan22359/Youtube_research-and_blog_writer_using_Crew.ai.git
cd Youtube_research-and_blog_writer_using_Crew.ai
```

### 2. Setup Environment
```bash
# Create virtual environment
python -m venv crew_ai_venv

# Activate virtual environment
# Windows
crew_ai_venv\Scripts\activate
# macOS/Linux
source crew_ai_venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Key
1. Get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)
2. Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the System
```bash
python crew.py
```

When prompted, enter any topic you want a blog post about (e.g., "artificial intelligence", "climate change", "cryptocurrency").

## 📁 Project Structure

```
├── agents.py           # AI agent definitions (researcher & writer)
├── tasks.py           # Task definitions for each agent
├── tools.py           # YouTube search and analysis tools
├── crew.py            # Main execution file
├── requirements.txt   # Python dependencies
├── .env              # API keys (create this file)
└── README.md         # Project documentation
```

## 🛠️ Core Components

### **AI Agents**
- **Blog Researcher**: Searches YouTube for relevant content and extracts insights
- **Blog Writer**: Creates engaging, well-structured blog posts from research

### **Tools**
- **YouTube Video Search**: Finds relevant videos by keywords
- **YouTube Channel Search**: Searches specific channels for content

### **Technologies**
- **CrewAI**: Multi-agent orchestration framework
- **Google Gemini**: Advanced language model
- **YouTube Tools**: Content discovery and analysis
- **Python**: Core programming language

## 📊 Example Output

Input: `"python programming"`

Output: A comprehensive blog post with:
- Introduction to Python
- Beginner concepts and syntax
- Intermediate programming topics
- Advanced applications
- Learning resources and tips
- Professional formatting in Markdown

## 🔧 Customization

### Modify Agent Personalities
```python
# In agents.py
blog_researcher = Agent(
    role='Your Custom Role',
    goal='Your Custom Goal',
    backstory="Your custom backstory..."
)
```

### Add New Tools
```python
# In tools.py
from crewai_tools import WebsiteSearchTool
website_tool = WebsiteSearchTool()
```

### Change Output Format
```python
# In tasks.py
expected_output="Your custom output format..."
```

## 📋 Requirements

- Python 3.8+
- Google Gemini API key
- Internet connection for YouTube access

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini AI API key | Yes |


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
