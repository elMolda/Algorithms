class Graph:
    
    def __init__(self, V, E):
            
        self.V = V
        self.E = E
        
    def __str__(self):
        
        graph_str = ''
        
        for start in self.E.keys():
            for stop in self.E[start]:
                graph_str += start + ' ' + stop + '\n'
                
        return graph_str
