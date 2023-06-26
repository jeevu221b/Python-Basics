# prob = [4, 1]
# op = ["-"]
# ans = 0

# if op[0] == "/":
#     ans = prob[0] / prob[1]
# elif op[0] == "*":
#     ans = prob[0] * prob[1]
# elif op[0] == "+":
#     ans = prob[0] + prob[1]
# else:
#     ans = prob[0] - prob[1]
# for i in range(2, len(prob)):
#     if op[i-1] == "/":
#         ans = ans / prob[i]
#     elif op[i-1] == "*":
#         ans = ans * prob[i]
#     elif op[i-1] == "+":
#         ans = ans + prob[i]
#     else:
#         ans = ans - prob[i]
# print(ans)
problem = "9+2-2"
length = len(problem)
op = []
prob = []
ans = 0
for i in range(length):
    if problem[i] == "/":
        op.append(problem[i])
    elif problem[i] == "*":
        op.append(problem[i])
    elif problem[i] == "+":
        op.append(problem[i])
    elif problem[i] == "-":
        op.append(problem[i])
    else:
        prob.append(int(problem[i]))

if op[0] == "/":
    ans = prob[0] / prob[1]
elif op[0] == "*":
    ans = prob[0] * prob[1]
elif op[0] == "+":
    ans = prob[0] + prob[1]
else:
    ans = prob[0] - prob[1]
for i in range(2, len(prob)):
    if op[i-1] == "/":
        ans = ans / prob[i]
    elif op[i-1] == "*":
        ans = ans * prob[i]
    elif op[i-1] == "+":
        ans = ans + prob[i]
    else:
        ans = ans - prob[i]
print(ans)
