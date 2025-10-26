from classes.agent import Agent
from classes.report import Report
from classes.missionControl import MissionControl
from classes.intelTools import IntelTools



agent1 = Agent("unit 8200" , 4)
report1 = Report("bla bla", 4, agent1)
print(report1.summary)
MissionControl.analyze_report(report1)
IntelTools.log_transmission(agent1.code_name, report1.summary)


