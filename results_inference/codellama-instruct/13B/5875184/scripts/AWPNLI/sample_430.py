premise_oil = 6522.0
premise_leaked = 5165.0
hypothesis_leaked = 1357.0

# the hypothesis refers to the amount of oil leaked, which is also mentioned in the premise
# compute the total amount of oil leaked from the premise
total_leaked_premise = premise_oil - premise_leaked
if total_leaked_premise!= hypothesis_leaked:
    # check if the amount of oil leaked in the hypothesis contradicts the amount of oil leaked from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
