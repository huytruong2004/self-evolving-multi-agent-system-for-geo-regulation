"""
Minimal Agent Factory for GeoFlow Compliance Detection System

Creates agents from configuration with fixed tools.
"""

from typing import List, Dict, Any
from deepagents import create_deep_agent
import logging
from src.tools import vector_search
from config.agent_config import AgentConfig
logger = logging.getLogger(__name__)

class AgentFactory:
    """
    Minimal factory for creating agents from configuration.
    
    Assumes fixed tools - no dynamic tool registration needed.
    """
    
    def __init__(self, config_path: str = "config/agents.yaml", agent_name: str = "geoflow"):
        """
        Initialize with config path and agent name.
        
        Args:
            config_path: Path to agents.yaml config file
            agent_name: Name of the main agent to create
        """
        self.config_path = config_path
        self.agent_name = agent_name
        self.agent_config = AgentConfig(config_path)
        self._load_config()
        
        logger.info(f"AgentFactory initialized with {len(self.subagents_config)} subagents")
    
    def _load_config(self):
        """Load configuration using AgentConfig class."""
        self.main_agent_config = self.agent_config.get_main_agent(self.agent_name)
        
        # Get subagent names from main agent config
        subagent_names = self.main_agent_config.get("subagents", [])
        
        # Load each subagent configuration
        self.subagents_config = []
        for subagent_name in subagent_names:
            subagent_config = self.agent_config.get_subagent(subagent_name)
            self.subagents_config.append(subagent_config)
    
    def create_agent(self, recursion_limit: int = 1000):
        """
        Create the main agent with all subagents.
        
        Args:
            recursion_limit: Recursion limit for the agent
            
        Returns:
            Configured main agent ready to use
        """
        # Fixed builtin tools
        builtin_tools = ["write_todos", "write_file", "read_file", "edit_file", "ls"]
        
        # Main agent gets vector_search tool
        main_tools = [vector_search]
        
        logger.info(f"Creating agent: {self.main_agent_config['name']}")
        
        # Create the agent
        agent = create_deep_agent(
            tools=main_tools,
            instructions=self.main_agent_config['instructions'],
            subagents=self.subagents_config,
            builtin_tools=builtin_tools
        ).with_config({"recursion_limit": recursion_limit})
        
        logger.info("Agent created successfully")
        return agent


def create_geoflow_agent(config_path: str = "config/agents.yaml", agent_name: str = "geoflow"):
    """
    Convenience function to create the GeoFlow agent.
    
    Args:
        config_path: Path to the configuration file
        agent_name: Name of the main agent to create
        
    Returns:
        Configured GeoFlow agent
    """
    factory = AgentFactory(config_path, agent_name)
    return factory.create_agent()
