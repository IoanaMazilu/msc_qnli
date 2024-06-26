peaches_left_premise = 34.0
peaches_picked_premise = 86.0
total_peaches_hypothesis = peaches_left_premise + peaches_picked_premise

# the hypothesis refers to the total number of peaches, which is also mentioned in the premise
if total_peaches_hypothesis!= 120.0:
    # check if the total number of peaches in the hypothesis contradicts the total number of peaches in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
