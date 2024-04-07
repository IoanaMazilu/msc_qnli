# Premise: Anusha, Banu and Esha run a running race of 100 meters.
# Hypothesis: Anusha, Banu and Esha run a running race of more than 100 meters.
# Golden Label: contradiction

race_distance_premise = 100
race_distance_hypothesis = 100

# the hypothesis refers to the same race distance mentioned in the premise
if race_distance_premise < race_distance_hypothesis:
    # check if the hypothesis value contradicts the race distance in the premise
    label = "contradiction"
elif race_distance_premise > race_distance_hypothesis:
    # check if the hypothesis value is less than the race distance in the premise
    label = "contradiction"
else:
    # if the hypothesis value and premise value are the same, we can infer entailment
    label = "entailment"

print(label)

