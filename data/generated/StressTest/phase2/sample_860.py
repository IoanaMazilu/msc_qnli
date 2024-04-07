# Premise: 4 buses runs between Chennai and Mysore.
# Hypothesis: 1 buses runs between Chennai and Mysore.
# Golden Label: contradiction

buses_premise = 4
buses_hypothesis = 1

# the hypothesis talks about the number of buses running between Chennai and Mysore, referenced also in the premise
if buses_hypothesis > buses_premise:
    # check if the hypothesis value contradicts the given number of buses in the premise
    label = "contradiction"
elif buses_hypothesis < buses_premise:
    # check if the hypothesis value is less than the given number of buses in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

