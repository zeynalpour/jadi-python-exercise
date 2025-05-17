from modules.mypriority import Priority


class Task:
    '''
    هر تسک توضیحات و نام و اولویت دارد
    '''
    def __init__(self, name, prio = Priority.Medium,  desc =  ""):
        self.name = name
        self.desc = desc
        self.prio = prio

    
    def update_name(self, name):
        self.name = name
        return self.name
    
    def update_description(self, desc):
        self.desc = desc
        return self.desc
    
    def update_priority(self, prio):
        self.prio = prio
        return self.prio
    
    def __str__(self):
        prio = self.prio
        print(prio)
        if prio == Priority.High: prio = "High" 
        elif prio == Priority.Medium: prio = "Medium" 
        elif prio == Priority.Low: prio = "Low" 
        elif prio == Priority.Unknown : prio = "unknown"
        return f"{self.name:<{15}}   |   {prio:^{25}}   |   {self.desc:<{45}}\n"
    
    def to_list(self):
        return self.name, self.prio,  self.desc