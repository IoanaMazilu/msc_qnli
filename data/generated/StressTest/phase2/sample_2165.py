# Premise: 4 buses runs between Chennai and Mysore.
# Hypothesis: more than 4 buses runs between Chennai and Mysore.
# Golden Label: contradiction

buses_premise = 4
buses_hypothesis = 4

# the hypothesis refers to the number of buses mentioned in the premise
if buses_hypothesis >= buses_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

