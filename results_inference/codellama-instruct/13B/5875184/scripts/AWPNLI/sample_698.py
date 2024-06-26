premise_peaches = 34.0
orchard_peaches = 86.0
hypothesis_peaches = 120.0

# the hypothesis refers to the total number of peaches, which are also mentioned in the premise
# compute the total number of peaches in the premise
total_peaches_premise = premise_peaches + orchard_peaches
if total_peaches_hypothesis!= total_peaches_premise:
    # check if the number of peaches in the hypothesis contradicts the number of peaches from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
