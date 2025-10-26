class Agent:

    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self.__clearence_level = clearance_level

    def report(self):
        print(f"Agent {self.code_name} reporting. clearence Level {self.__clearence_level}")

    def get_clearance_level(self):
        return self.__clearence_level
    
    def set_clearence_level(self, level: int):
        if 1 < level < 5:
            self.__clearence_level = level
        else:
            print("Error seting agent, setting values have below 1 or above 5")



