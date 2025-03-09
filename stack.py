class stack:
    def __init__(s):
        s.arr = []
    def push(s, var): 
        s.arr.append(var)
    def __repr__(s):  
        return f"{s.arr}"
    def pop(s):
        s.arr.remove(s.arr[-1])
    def isempty(s):
        if (len(s.arr) == 0):
            return True
        else:
            return False