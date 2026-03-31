class SlotManager:
    def __init__(self, max_slot):
        self.parent = [i for i in range(max_slot + 1)]

    def find(self, slot):
        if self.parent[slot] == slot:
            return slot
        self.parent[slot] = self.find(self.parent[slot])
        return self.parent[slot]

    def occupy(self, slot):
        self.parent[slot] = self.find(slot - 1)


class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        n=len(deadline)
        jobs=[(profit[i],deadline[i]) for i in range(n)]
        jobs.sort(key=lambda job :job[0],reverse=True)
        total_job=0
        total_profit=0
        slt=SlotManager(n)
        for profit,deadline in jobs :
             sloat=slt.find(deadline)
             if(sloat>0) :
                    total_job+=1
                    total_profit+=profit
                    
                    slt.occupy(sloat)
        return [total_job,total_profit]
                 
                 
            
            
