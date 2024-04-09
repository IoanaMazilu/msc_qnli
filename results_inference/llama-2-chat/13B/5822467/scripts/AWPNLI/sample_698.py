peaches_premise = 34.0
peaches_hypothesis = 120.0

# compute the total number of peaches in the premise
total_peaches_premise = peaches_premise + 86.0

if peaches_hypothesis > total_peaches_premise:
    # check if the number of peaches in the hypothesis contradicts the number of peaches from the premise
    label = "contradiction"
elif peaches_hypothesis!= total_peaches_premise:
    # check if the number of peaches in the hypothesis contradicts the number of peaches from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
