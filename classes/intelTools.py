class IntelTools:

    @staticmethod
    def encrypt_massage(msg: str) -> str: 
        return msg[::-1]
    
    @staticmethod
    def log_transmission(agent_name: str, massage: str) -> None:
        print(f"{agent_name} send encrypted message: {IntelTools.encrypt_massage(massage)}")

    