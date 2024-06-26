premise_oil_leaked = 6522.0
hypothesis_oil_leaked = 1358.0

# the hypothesis refers to the number of liters of oil leaked, which is also mentioned in the premise
# compute the total number of liters of oil leaked in the premise
total_oil_leaked_premise = premise_oil_leaked - hypothesis_oil_leaked
if total_oil_leaked_premise!= 0:
    # check if the number of liters of oil leaked from the hypothesis contradicts the number of liters leaked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
