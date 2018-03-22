class MaxDrawdown():
    def __init__(self, data):
        self.data = data.dropna().copy()
        self.data_cum = self.data.cumsum()
        
    def max_drawdown(self):
        d = self.data_cum
        idmax = 0
        drawdown = [0, 0, 0, 0]
        
        for i in range(len(d)):
            if d[i] > d[idmax]:
                idmax = i
            if d[idmax] - d[i] >= drawdown[0]:
                drawdown[0] = d[idmax] - d[i]
                drawdown[2] = idmax
                drawdown[3] = i
            
        drawdown[1] = 1 - (1 + self.data.iloc[drawdown[2]:drawdown[3]+1]).prod()
        drawdown[2] = d.index[drawdown[2]]
        drawdown[3] = d.index[drawdown[3]]

        return drawdown
