class queue:
    def __init__(s):
        s.arr = []
    def __repr__(s):
        return f"{s.arr}"
    def push(s, var):
        s.arr.append(var)
    def pop(s):
        s.arr.remove(s.arr[0])
    def isempty(s):
        if (len(s.arr) == 0):
            return True
        else:
            return False