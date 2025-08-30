# GeoFlow Compliance Detection System - Sub-Agent Loader

"""
Sub-agent configuration loader for the GeoFlow Compliance Detection System.

This module provides backward compatibility by loading sub-agent configurations
from the centralized agents.yaml file instead of hardcoded definitions.

DESIGN PRINCIPLES:
- Centralized configuration management via agents.yaml
- Backward compatibility with existing imports
- Separation of configuration from code logic
"""

from config.agent_config import AgentConfig

# Load configuration instance
config = AgentConfig()

# Export sub-agents list for backward compatibility
# This maintains the same interface as the original hardcoded COMPLIANCE_SUBAGENTS
COMPLIANCE_SUBAGENTS = config.get_subagents_for_main("geoflow")

# Individual agent exports for direct access if needed
regulatory_expert_agent = config.get_subagent("regulatory-expert")
compliance_critic_agent = config.get_subagent("compliance-critic")