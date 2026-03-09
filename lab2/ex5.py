'''
6. Simulate a Markov(nu stiu daca am scris cum trebuie)  machine conaining 3 states A,B,C:in the image; Run this machine 15 times and record the sequence of states. 
Store these states as "S": Each state carries a weight: 

A: 1.5
B: 2
C: 3.3

Use these weights as values for the growth factor r, and calculate the population size on 15 steps

according to the weights form S. Start the population from 0.5
'''

import random

# markov chain
transitions = {
    'A': {'A': 0.0, 'B': 0.4, 'C': 0.6},
    'B': {'A': 0.5, 'B': 0.5, 'C': 0.0},
    'C': {'A': 0.2, 'B': 0.2, 'C': 0.6}
}

weights = {
    'A': 1.5,
    'B': 2.0,
    'C': 3.3
}

#Markov Machine for 15 steps
#i will start randomly at state 'A'.
current_state = 'A'
sequence_S = []

for _ in range(15):
    sequence_S.append(current_state)
    
    #probabilities for the next state
    next_states = list(transitions[current_state].keys())
    probs = list(transitions[current_state].values())
    
    #next state based on the probabilities
    current_state = random.choices(next_states, weights=probs, k=1)[0]

#calculate the population size over the 15 steps
x = 0.5  # Starting population ratio
population_history = [x]

print("\n" + "="*50)
print(" MARKOV CHAIN POPULATION SIMULATION (15 STEPS)")
print("="*50)
print(f"Initial Population: x_0 = {x}\n")

for i, state in enumerate(sequence_S):
    r = weights[state]
    
    x_next = r * x * (1 - x)
    population_history.append(x_next)
    
    print(f"Step {i+1:2d} | State: {state} | r: {r:3.1f} | Population (x): {x_next:.6f}")
    
    # Update x for the next loop
    x = x_next

print("="*50 + "\n")