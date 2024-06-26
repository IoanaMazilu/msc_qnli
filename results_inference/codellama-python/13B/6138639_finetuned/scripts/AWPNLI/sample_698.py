peaches_left_premise = 34.0
peaches_picked_premise = 86.0
total_peaches_hypothesis = 120.0

# the hypothesis refers to the total number of peaches, which are also mentioned in the premise
# compute the total number of peaches in the premise
total_peaches_premise = peaches_left_premise + peaches_picked_premise
if total_peaches_hypothesis!= total_peaches_premise:
    # check if the total number of peaches in the hypothesis contradicts the total number of peaches from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
