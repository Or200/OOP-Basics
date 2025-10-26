from agent import *

class Mission:

    def __init__(self, mission_name: str, target_location: str):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = None

    def assigned_agent_fnuc(self, agent: Agent):
        self.assigned_agent = agent

    def brief(self):
        print(f"Mission: {self.mission_name}, Target; {self.target_location}, Agent: {Agent.code_name}")

    

    
