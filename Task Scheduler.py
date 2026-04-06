from heapq import *
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], k: int) -> int:
        freq = []
        mp = {}

        for task in tasks:
            if task in mp:
                mp[task] += 1
            else:
                mp[task] = 1

        for task in mp:
            freq.append(-mp[task])

        heapify(freq)
        heap = freq
        total_time = 0

        while heap:
            f = heappop(heap)

            if len(heap) >= k:
                temp = []
                for _ in range(k):
                    ff = heappop(heap)
                    if ff != -1:
                        temp.append(ff + 1)

                for e in temp:
                    heappush(heap, e)

                total_time += (k + 1)

            else:
                temp = []
                while heap:
                    ff = heappop(heap)
                    temp.append(ff)

                time = 1
                for e in temp:
                    time += 1
                    if e != -1:
                        heappush(heap, e + 1)

                if f == -1 and not heap:
                    total_time += time
                else:
                    total_time += (k + 1)

            if f != -1:
                heappush(heap, f + 1)

        return total_time
