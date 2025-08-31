> An intelligent multi-agent system that leverages genetic algorithms and deep learning to analyze geo-specific regulatory compliance across jurisdictions.

## 🌟 Features

- **🧬 Self-Evolving Architecture**: Genetic algorithm-based agent improvement system
- **👥 Specialized Sub-Agents**: 5 expert agents for regulatory analysis
- **🔍 Vector Search**: Semantic search over regulatory document collections
- **🌐 Real-Time UI**: Interactive chat interface with agent visualization
- **🔄 Human-in-the-Loop**: Feedback integration for continuous improvement
- **📊 Comprehensive Analysis**: Multi-jurisdictional compliance assessment
- **⚡ Parallel Processing**: Concurrent task execution and delegation

## 📋 Table of Contents

- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Development](#development)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GeoFlow System Architecture              │
├─────────────────────────────────────────────────────────────┤
│  Frontend (Next.js)                                         │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│  │   Chat UI       │  │  Agent Monitor  │  │  Task View  │  │
│  └─────────────────┘  └─────────────────┘  └─────────────┘  │
├─────────────────────────────────────────────────────────────┤
│  LangGraph Server                                           │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                 GeoFlow Agent                          │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │ │
│  │  │ Researcher  │  │   Critic    │  │  Sub-Agents     │ │ │
│  │  └─────────────┘  └─────────────┘  └─────────────────┘ │ │
│  └────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  Core Components                                            │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│  │  Deep Agents    │  │   ChromaDB      │  │  Model Hub  │  │
│  │  - Regulatory   │  │  (Vector DB)    │  │  - OpenAI   │  │
│  │  - Risk         │  │                 │  │  - Google   │  │
│  │  - Compliance   │  │                 │  │  - Tavily   │  │
│  │  - Engineer     │  │                 │  │             │  │
│  └─────────────────┘  └─────────────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Core Components

#### Backend (Python)
- **deepagents/**: Core agent system with graph-based workflow orchestration
  - `graph.py`: Agent creation and workflow management
  - `sub_agent.py`: Sub-agent task delegation
  - `model.py`: Model configuration and defaults
  - `tools.py`: File operations and task management
  - `state.py`: Agent state management
  - `interrupt.py`: Human intervention handling

- **multi-agent.py**: Main GeoFlow agent entry point
- **ChromaDB**: Vector database for regulatory document storage

#### Frontend (Next.js)
- **deep-agents-ui/**: React application for agent interaction
- **TypeScript**: Type-safe development
- **Tailwind CSS + Radix UI**: Modern component library
- **Real-time Chat**: Markdown rendering with syntax highlighting
- **Agent Visualization**: Sub-agent progress tracking

## 📋 Prerequisites

- **Python**: 3.11 or higher
- **Node.js**: 18 or higher
- **npm**: 9 or higher
- **Git**: For version control

### API Keys Required
- OpenAI API key (for GPT models)
- Google API key (for embeddings)
- Tavily API key (for web search)
- LangSmith API key (optional, for monitoring)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/self-evolving-multi-agent-system-for-geo-regulation.git
cd self-evolving-multi-agent-system-for-geo-regulation
```

### 2. Backend Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd deep-agents-ui

# Install Node.js dependencies
npm install
```

## ⚙️ Configuration

### 1. Backend Environment Variables

Create `.env` file in the project root:

```env
# API Keys
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
LANGSMITH_API_KEY=your_langsmith_api_key

# Database Configuration
CHROMA_DB_PATH=./chroma_db

# LangGraph Configuration
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=geoflow-system
```

### 2. Frontend Environment Variables

Create `deep-agents-ui/.env.local`:

```env
NEXT_PUBLIC_DEPLOYMENT_URL=http://localhost:8123
NEXT_PUBLIC_AGENT_ID=agent
NEXT_PUBLIC_LANGSMITH_API_KEY=your_langsmith_api_key
```

### 3. Agent Configuration

The system uses `config/agents.yaml` to define agent behaviors:

```yaml
regulatory-expert:
  role: "Regulatory Expert"
  expertise: "Geo-specific regulatory analysis"
  tools: ["search", "analyze"]

risk-resolver:
  role: "Risk Assessment Specialist"
  expertise: "Compliance risk evaluation"
  tools: ["assess", "mitigate"]

# Additional agents...
```

## 🎯 Usage

### 1. Start the Backend

```bash
# Start LangGraph server
langgraph dev

# The server will start on http://localhost:8123
```

### 2. Start the Frontend

```bash
# In a new terminal
cd deep-agents-ui
npm run dev

# Access the UI at http://localhost:3000
```

## 🛠️ Development

### Adding New Agents

1. **Define Agent Configuration** in `config/agents.yaml`:
```yaml
new-agent:
  role: "New Agent Role"
  expertise: "Specific domain expertise"
  tools: ["tool1", "tool2"]
```

2. **Implement Agent Logic** in `deepagents/`:
```python
class NewAgent:
    def __init__(self, config):
        self.config = config
    
    def process(self, query):
        # Agent processing logic
        return result
```

### Extending the System

- **Add New Tools**: Extend `deepagents/tools.py`
- **Modify UI**: Update components in `deep-agents-ui/src/`
- **Custom Models**: Configure in `deepagents/model.py`

## 🙏 Acknowledgments

- [LangChain](https://langchain.com) for the agent framework
- [LangGraph](https://langgraph-sdk.python.langchain.com) for workflow orchestration
- [Next.js](https://nextjs.org) for the frontend framework
- [ChromaDB](https://www.trychroma.com) for vector database capabilities

---

<p align="center">
  Made with ❤️ for regulatory compliance and AI innovation
</p>