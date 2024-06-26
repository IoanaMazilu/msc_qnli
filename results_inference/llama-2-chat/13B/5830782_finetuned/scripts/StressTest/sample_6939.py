floor_premise = 51
floor_hypothesis = 61
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the floor and rate of descent of the elevator mentioned in the premise
if floor_premise >= floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of descent in the hypothesis contradicts the rate of descent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
