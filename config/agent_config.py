"""
Agent Configuration Loader for GeoFlow CDS

This module provides utilities for loading agent configurations from YAML files,
allowing centralized management of agent properties while keeping model 
configurations in code.
"""

import yaml
from typing import Dict, List, Optional, Any
import os


class AgentConfig:
    """
    Configuration loader for GeoFlow agents.
    
    Loads agent configurations from YAML files and provides methods to retrieve
    main agent and subagent configurations with proper model defaults.
    """
    
    def __init__(self, config_path: str = "config/agents.yaml"):
        """
        Initialize the configuration loader.
        
        Args:
            config_path (str): Path to the YAML configuration file
        """
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            if not config:
                raise ValueError(f"Empty configuration file: {self.config_path}")
            
            return config
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in configuration file {self.config_path}: {e}")
        except Exception as e:
            raise RuntimeError(f"Error loading configuration from {self.config_path}: {e}")
    
    def get_main_agent(self, agent_name: str) -> Dict[str, Any]:
        """
        Get main agent configuration.
        
        Args:
            agent_name (str): Name of the main agent (e.g., "geoflow")
            
        Returns:
            Dict[str, Any]: Main agent configuration
            
        Raises:
            KeyError: If agent not found in configuration
        """
        if "main_agents" not in self.config:
            raise KeyError("No 'main_agents' section found in configuration")
        
        if agent_name not in self.config["main_agents"]:
            available = list(self.config["main_agents"].keys())
            raise KeyError(f"Main agent '{agent_name}' not found. Available: {available}")
        
        return self.config["main_agents"][agent_name].copy()
    
    def get_subagent(self, subagent_name: str, include_model: bool = True) -> Dict[str, Any]:
        """
        Get subagent configuration.
        
        Args:
            subagent_name (str): Name of the subagent
            include_model (bool): Whether to include default model configuration
            
        Returns:
            Dict[str, Any]: Subagent configuration with model defaults
            
        Raises:
            KeyError: If subagent not found in configuration
        """
        if "subagents" not in self.config:
            raise KeyError("No 'subagents' section found in configuration")
        
        if subagent_name not in self.config["subagents"]:
            available = list(self.config["subagents"].keys())
            raise KeyError(f"Subagent '{subagent_name}' not found. Available: {available}")
        
        subagent = self.config["subagents"][subagent_name].copy()
        
        # Add default model configuration if requested and not already present
        if include_model and "model" not in subagent:
            subagent["model"] = {
                "model": "o4-mini",
                "model_provider": "openai"
            }
        
        return subagent
    
    def get_subagents_for_main(self, agent_name: str) -> List[Dict[str, Any]]:
        """
        Get list of subagents configured for a main agent.
        
        Args:
            agent_name (str): Name of the main agent
            
        Returns:
            List[Dict[str, Any]]: List of subagent configurations
        """
        main_agent = self.get_main_agent(agent_name)
        subagent_names = main_agent.get("subagents", [])
        
        return [self.get_subagent(name) for name in subagent_names]
    
    def list_main_agents(self) -> List[str]:
        """
        Get list of available main agent names.
        
        Returns:
            List[str]: List of main agent names
        """
        return list(self.config.get("main_agents", {}).keys())
    
    def list_subagents(self) -> List[str]:
        """
        Get list of available subagent names.
        
        Returns:
            List[str]: List of subagent names
        """
        return list(self.config.get("subagents", {}).keys())
    
    def reload_config(self) -> None:
        """Reload configuration from file."""
        self.config = self._load_config()


# Default instance for easy importing
default_config = AgentConfig()