class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        max_count = max(counts.values())
        counts = list(counts.values())
        max_counts_elements = 0
    
        for i in range(0, len(counts)):
            if(counts[i]) == max_count:
                max_counts_elements += 1
        
        val = (max_count-1)*(n+1)+max_counts_elements
        
        return max(val, len(tasks))
