# Premise: Sourav walks 20 meters towards North.
# Hypothesis: Sourav walks more than 20 meters towards North.
# Golden Label: contradiction

distance_walked_premise = 20
distance_walked_hypothesis = 20

# The hypothesis refers to the distance walked by Sourav mentioned in the premise
if distance_walked_hypothesis >= distance_walked_premise:
    # check if 'distance_walked_hypothesis' contradicts the distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis value doesn't contradict the premise one, we infer entailment
    label = "entailment"
    
print(label)

