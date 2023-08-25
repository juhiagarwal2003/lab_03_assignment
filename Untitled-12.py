#Juhi Agarwal E22CSEU0925
class Process:
    def __init__(self, pid, name, start_time, priority):
        self.pid = pid
        self.name = name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []
        
    def add_process(self, process):
        self.processes.append(process)
        
    def print_table(self):
        for process in self.processes:
            print(f'P_ID: {process.pid}, Process: {process.name}, Start Time: {process.start_time}, Priority: {process.priority}')
            
    def sort_by_pid(self):
        self.processes.sort(key=lambda process: process.pid)
        
    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)
        
    def sort_by_priority(self):
        self.processes.sort(key=lambda process: process.priority, reverse=True)

if __name__ == "__main__":
    flight_table = FlightTable()
    
    flight_table.add_process(Process('P1', 'VSCode', 100, 'MID'))
    flight_table.add_process(Process('P23', 'Eclipse', 234, 'MID'))
    flight_table.add_process(Process('P93', 'Chrome', 189, 'High'))
    flight_table.add_process(Process('P42', 'JDK', 9, 'High'))
    flight_table.add_process(Process('P9', 'CMD', 7, 'High'))
    flight_table.add_process(Process('P87', 'NotePad', 23, 'Low'))
    
    sorting_options = {
        1: flight_table.sort_by_pid,
        2: flight_table.sort_by_start_time,
        3: flight_table.sort_by_priority
    }
    
    print("Choose a sorting parameter:")
    print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority")
    choice = int(input("Enter your choice: "))
    
    if choice in sorting_options:
        sorting_options[choice]()
        flight_table.print_table()
    else:
        print("Invalid choice")
