import json
from typing import Dict, Optional, Any

# Mapping of PeixotoClaw agents to model for each profile
MODEL_PROFILES = {
    'architect': { 
        'quality': 'claude-3-5-sonnet', 
        'balanced': 'gemini-1.5-pro', 
        'budget': 'gemini-1.5-flash' 
    },
    'builder': { 
        'quality': 'claude-3-5-sonnet', 
        'balanced': 'gemini-1.5-pro', 
        'budget': 'gemini-1.5-flash' 
    },
    'pm': { 
        'quality': 'gemini-1.5-pro', 
        'balanced': 'gemini-1.5-flash', 
        'budget': 'gemini-1.5-flash' 
    },
    'auditor': { 
        'quality': 'claude-3-5-sonnet', 
        'balanced': 'gemini-1.5-pro', 
        'budget': 'gemini-1.5-flash' 
    }
}

VALID_PROFILES = ['quality', 'balanced', 'budget']

def get_model_for_agent(agent_name: str, profile: str = 'balanced') -> str:
    """
    Returns the recommended model for a given agent and profile.
    Implements fallback logic if the agent name is unknown.
    """
    agent_key = agent_name.lower().replace('@', '')
    
    if profile not in VALID_PROFILES:
        profile = 'balanced'
        
    if agent_key in MODEL_PROFILES:
        return MODEL_PROFILES[agent_key][profile]
    
    # Default fallback
    return 'gemini-1.5-flash' if profile == 'budget' else 'gemini-1.5-pro'

def get_fallback_model(current_model: str) -> str:
    """
    Returns a fallback model if the current one stalls or hits limits.
    """
    fallbacks = {
        'claude-3-5-sonnet': 'gemini-1.5-pro',
        'claude-3-opus': 'claude-3-5-sonnet',
        'gemini-1.5-pro': 'gemini-1.5-flash',
        'gemini-1.5-flash': 'claude-3-5-sonnet' # Retry cycle
    }
    return fallbacks.get(current_model, 'gemini-1.5-pro')

def get_profile_mapping(profile: str) -> Dict[str, str]:
    """Returns the full mapping for a profile."""
    if profile not in VALID_PROFILES:
        profile = 'balanced'
    return {agent: models[profile] for agent, models in MODEL_PROFILES.items()}
