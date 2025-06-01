
import pickle
# Load name-based graph
with open("id_to_id_author_mapping_with_probs.pkl", "rb") as f:
    graph = pickle.load(f)



import pickle
import random
from collections import defaultdict



def process_top_k(top_k):
    # Extract keys (first elements of each tuple)
    keys = [item[0] for item in top_k]
    
    # Sum of the values (second elements of each tuple)
    total_value_sum = sum(item[1] for item in top_k)
    
    return keys, total_value_sum

def independent_cascade(graph, seed, steps=100):
    spread = 0
    for _ in range(steps):
        active = set([seed])
        for neighbor, prob in graph.get(seed, []):
            if neighbor not in active and random.random() <= prob:
                active.add(neighbor)
        spread += len(active)
    return spread / steps  # average influence

# Ask user for top-k value
try:
    k = int(input("Enter how many top influential authors you want to retrieve: "))
except ValueError:
    print("Invalid input. Using default value of 10.")
    k = 10  # default fallback

# Compute influence scores
influence_scores = {}
c = 0
for node in graph:
    influence_scores[node] = independent_cascade(graph, node, steps=100)
    c += 1
    #print(f"{c} node completed")

# Get top-k as a dictionary
top_k_sorted = sorted(influence_scores.items(), key=lambda x: x[1], reverse=True)[:k]
#top_k_dict = {node_id: round(spread, 2) for node_id, spread in top_k_sorted}


keys, value_sum = process_top_k(top_k_sorted)

print("Top k influencers id are :", keys)
print("Expected Influence spread =", value_sum)
