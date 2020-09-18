class Calculate:
    def __init__(self,data):
        self.data = data

    def get_result(self):
        temp = self.data.operator
        if temp == '+': return (self.data.parameterA + self.data.parameterB)
        if temp == '-': return (self.data.parameterA - self.data.parameterB)
        if temp == '*': return (self.data.parameterA * self.data.parameterB)
        if temp == '/': return (self.data.parameterA / self.data.parameterB)
