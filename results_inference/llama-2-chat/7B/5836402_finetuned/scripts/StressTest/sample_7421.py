floor_premise_1 = 11
floor_premise_2 = 81
floor_rate_premise = 57

floor_hypothesis_1 = 81
floor_hypothesis_2 = 11
floor_rate_hypothesis = 57

# the hypothesis refers to the floor number and the rate of elevator ride mentioned in the premise
if floor_premise_1!= floor_hypothesis_1:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif floor_rate_premise!= floor_rate_hypothesis:
    # check if the rate of elevator ride in the hypothesis contradicts the rate of elevator ride in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
