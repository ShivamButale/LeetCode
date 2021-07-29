class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y =  int(a, 2), int(b, 2)
        return bin(x+y).replace("0b","")
