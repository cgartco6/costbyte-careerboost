import time
import random

class DeepAgentsManager:
    def __init__(self):
        self.agent_status = {}

    def run_agent(self, agent_name, task_callable, *args):
        try:
            result = task_callable(*args)
            self.agent_status[agent_name] = "SUCCESS"
            return result
        except Exception as e:
            self.agent_status[agent_name] = "FAILED"
            time.sleep(1)
            return f"Agent {agent_name} failed: {e}"

    def status(self):
        return self.agent_status
