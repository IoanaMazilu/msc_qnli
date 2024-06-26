# the hypothesis refers to the walking rates of Matthew and Johnny
# the premise gives the walking rates of Matthew and Johnny

# the hypothesis is about the walking distance of Johnny when they met
# the premise gives the walking distance of Johnny when they met

# the hypothesis is consistent with the premise, but the exact distance cannot be inferred from the premise
# therefore, the label is neutral

distance_hypothesis = 3
distance_premise = 4

# the hypothesis states a different walking distance for Johnny than the premise
if distance_hypothesis == distance_premise:
    # if the hypothesis value and the premise value are the same, then it's an entailment
    label = "entailment"
else:
    # if the hypothesis value is different from the premise value, then it's a contradiction
    label = "contradiction"

print(label)
