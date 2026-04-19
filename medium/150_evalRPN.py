def operator(t1:int,t2:int,op:str)->int:
    if op=="+":
        return t1+t2
    elif op=="-":
        return t1-t2
    elif op=="*":
        return t1*t2
    elif op=="/":
        if t2==0:
            return False
        else:
            return t1/t2
def get_Prio(op:str):
    if op=="*" or op=="/":
        return 1
    else:
        return 0
def evalRPN( tokens: list[str]) -> int:
    stake_nums=[]
    res=0
    if len(tokens)==1:
        return int(tokens[0])
    for i,e in enumerate(tokens):
        if e not in ["+","-","*","/"]:
            stake_nums.append(e)
        else:
            t2=stake_nums.pop()
            t1=stake_nums.pop()
            res=operator(int(t1),int(t2),e)
            stake_nums.append(res)
    return res


token = ["2","1","+","3","*"]
t=evalRPN(token)
print(t)
token = ["4","13","5","/","+"]
t=evalRPN(token)
print(t)

token = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
t=evalRPN(token)
print(t)
token = ["10"]
t=evalRPN(token)
print(t)
token =["0","3","/"]
t=evalRPN(token)
print(t)