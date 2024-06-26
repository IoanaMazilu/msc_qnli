liters_oil_premise = 6522.0
liters_leaked_premise = 5165.0
liters_hypothesis = 1358.0

# the hypothesis refers to the number of liters leaked, which is also mentioned in the premise
# compute the number of liters leaked in the premise
liters_leaked_premise = liters_oil_premise - liters_leaked_premise
if liters_hypothesis!= liters_leaked_premise:
    # check if the number of liters leaked in the hypothesis contradicts the number of liters leaked from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
