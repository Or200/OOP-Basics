class IntelTools:

    @staticmethod
    def encrypt_massage(msg: str):
        return msg[::-1]
    
    @staticmethod
    def log_transmission(agent_name: str, massage: str):
        print(f"{agent_name} send encrypted message: {massage}")

    