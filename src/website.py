class Website:
    def __init__(self, data):
        self.parse(data)
        
    def parse(self, data):
        parts = data.strip().split('|')
        self.name = parts[0]
        self.url = parts[1]
        self.state = parts[2]
        
    def get_state(self):
        if self.state is None:
            return 0
        elif not self.state:
            return 0
        return int(float(self.state))
        
    def is_up(self):
        return self.state == "2"
    
    def is_down(self):
        return self.state == "1"
