import dilema
import random

firm1 = dilema.Firm()
firm2 = dilema.Firm()
firm1.create()
firm2.create()

epsilon = 1 #rate at which it randomly explores
"""
for i in range(1000): #number of iterations at each price set
    if(epsilon > random.random()): #should we explore or not
        action1 = random.randint(0, 2)
        action2 = random.randint(0, 2)
        firm1.run(action1, action2)
        firm2.run(action2, action1)
    else:
        action1 = firm1.best_action()
        action2 = firm2.best_action()
        firm1.run(action1, action2)
        firm2.run(action2, action1)
    epsilon -= .001

def nash_equilibrium(firm1n, firm2n):
    output = []
    for i in range (len(firm1n)):
        if firm1n[i] == firm2n[i]:
            output.append((firm1n[i], firm2n[i]))
    return output



print(firm1.best_action(), "\n", firm1.printp())
print(firm1.getq())
print(firm2.find_nash())
print()
print(firm2.best_action(), "\n", firm2.printp())
print(firm2.getq())
print(firm1.find_nash())
print()
"""
print(firm1.printp())
print(firm1.find_nash())
print(firm2.printp())
print(firm2.find_nash())
#print(nash_equilibrium(firm1.find_nash(), firm2.find_nash()))
