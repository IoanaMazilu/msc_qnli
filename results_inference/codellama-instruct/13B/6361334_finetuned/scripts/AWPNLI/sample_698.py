peaches_premise = 34.0
peaches_orchard_premise = 86.0
peaches_hypothesis = 120.0

# the hypothesis refers to the total number of peaches, which are also mentioned in the premise
# compute the total number of peaches in the premise
total_peaches_premise = peaches_premise + peaches_orchard_premise
if total_peaches_hypothesis!= total_peaches_premise:
    # check if the number of peaches in the hypothesis contradicts the number of peaches from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
