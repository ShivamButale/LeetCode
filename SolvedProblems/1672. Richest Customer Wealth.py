class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m_w = 0
        for i in accounts:
            m_w = max(m_w, sum(i))         
        return m_w
