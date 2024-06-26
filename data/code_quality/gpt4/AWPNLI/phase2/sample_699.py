initial_peaches_premise = 34.0
picked_peaches_premise = 86.0
total_peaches_hypothesis = 115.0

# the hypothesis refers to the total number of peaches, which is also mentioned in the premise
# compute the total number of peaches in the premise
total_peaches_premise = initial_peaches_premise + picked_peaches_premise
if total_peaches_hypothesis != total_peaches_premise:
    # check if the total number of peaches in the hypothesis contradicts the total number of peaches from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
