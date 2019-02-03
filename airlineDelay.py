
"""
Created on Sat Feb  2 10:40:22 2019

@author: Bharathy
"""

from pulp import *

#Create a list of all airport nodes
nodes = ['MSN', 'ORD', 'DTW', 'MSP', 'SFO', 'IAH', 'DCA', 'MCO']

#Create a dictionary with travel times
time = {('MSN','ORD'): 22, ('MSN','DTW'): 65, ('MSN', 'MSP'): 46, ('MSP', 'SFO'): 213, ('MSP','IAH'): 139,
          ('MSP','DCA'): 125, ('MSP','MCO'): 176, ('ORD','SFO'): 247, ('ORD','IAH'): 124, ('ORD', 'DCA'): 82,         
         ('ORD', 'MCO'): 135, ('DTW','SFO'): 280, ('DTW', 'IAH'): 147, ('DTW', 'DCA'):53, ('DTW', 'MCO'): 130
         }

#Create a lits of all the hubs, destinations and airlines
hub = ['ORD', 'DTW', 'MSP']
destination = ['SFO','IAH','DCA','MCO']
airline = ['United', 'Delta']

#Create a dictinary of delay times at the hub
delay = {
        'ORD': 180,
        'DTW': 90,
        'MSP': 190        
        }

#Create a list of tuples with possible routes
arcs = [('MSN','ORD'), ('MSN','DTW'), ('MSN', 'MSP'),('MSP', 'SFO'), ('MSP','IAH'),
          ('MSP','DCA'), ('MSP','MCO'), ('ORD','SFO'), ('ORD','IAH'), ('ORD', 'DCA'),         
         ('ORD', 'MCO'), ('DTW','SFO'), ('DTW', 'IAH'), ('DTW', 'DCA'),('DTW', 'MCO')     
       ]

#Creates the problem variable 'prob' to have all the problem data
prob = LpProblem('Minimize time', LpMinimize)

#Creates the variable 'x' that determines the number of times a route is used
x = pulp.LpVariable.dicts('Route',arcs, lowBound = 0, cat = LpInteger)

#Creates the binary variable 'u' that determines if a airline is used or not
u = pulp.LpVariable.dicts('Airline',airline,lowBound = 0,upBound = 1, cat =LpInteger)

#Objective function. To minimize the traveling time and delay time
prob += lpSum([x[a]*time[a] for a in arcs]) + lpSum([x['MSN',h]* delay[h] for h in hub])

#Constraints
#Balance equation to make sure arrival into and departure from a hub is equal
for h in hub :
    prob += (lpSum(x[h,d] for d in destination) - lpSum(x['MSN',h])) == 0
    
#Following two constraints ensures only one airline is selected 
prob += x['MSN', 'ORD'] == u['United']*4
prob += x['MSN', 'DTW'] + x['MSN','MSP'] == (u['Delta']*4)

#Constraint to make sure a destination is visited once
for d in destination :
    prob += lpSum(x[h,d] for h in hub) == 1
    
prob.solve()

#Print the routes that are used
for a in arcs:
    if x[a].value() > 0:
        print (x[a],x[a].value())

     

