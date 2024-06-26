start_floor_premise = 51
start_floor_hypothesis = 61
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the starting floor and the rate of descent of an elevator mentioned in the premise
if start_floor_hypothesis <= start_floor_premise:
    # check if the hypothesis value contradicts the starting floor in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of descent in the hypothesis contradicts the rate of descent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
