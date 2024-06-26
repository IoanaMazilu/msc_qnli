peaches_left_premise = 34.0
peaches_picked_premise = 86.0
peaches_total_hypothesis = 120.0

# the hypothesis refers to the total number of peaches, which is also mentioned in the premise
# compute the total number of peaches in the premise
peaches_total_premise = peaches_left_premise + peaches_picked_premise
if peaches_total_hypothesis!= peaches_total_premise:
    # check if the total number of peaches in the hypothesis contradicts the total number of peaches in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
