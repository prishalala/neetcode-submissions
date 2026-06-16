from typing import List
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record=[]
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit():
                record.append(int(operations[i]))
            elif operations[i].isalnum():
                if operations[i]=='C':
                    record.pop()
                elif operations[i]=='D':
                    record.append((record[-1])*2)
            elif operations[i]=='+':
                record.append(record[-1]+record[-2])
        
        return sum(record)
