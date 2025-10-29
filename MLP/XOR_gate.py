def OR_gate(x1, x2):
    w1 = 0.6
    w2 = 0.6
    b = -0.5
    result = x1*w1 + x2*w2 + b
    if result <= 0:
        return 0
    else:
        return 1


def AND_gate(x1, x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.7
    result = x1*w1 + x2*w2 + b
    if result <= 0:
        return 0
    else:
        return 1

def NAND_gate(x1, x2):
    w1 = -0.5
    w2 = -0.5
    b = 0.7
    result = x1*w1 + x2*w2 + b
    if result <= 0:
        return 0
    else:
        return 1

x1 = NAND_gate(0, 0)
x2 =OR_gate(0,0)
print(x1,",",x2,"= ",AND_gate(x1,x2))  # 0,0 0

x1 = NAND_gate(0, 1)
x2 =OR_gate(0,1)
print(x1,",",x2,"= ",AND_gate(x1,x2))  # 0,1 1

x1 = NAND_gate(1, 0)
x2 =OR_gate(1,0)
print(x1,",",x2,"= ",AND_gate(x1,x2))  # 0,1 1

x1 = NAND_gate(1, 1)
x2 =OR_gate(1,1)
print(x1,",",x2,"= ",AND_gate(x1,x2)) # 0,1 1
