total_oil_premise = 6522.0 - 5165.0
leaked_oil_hypothesis = 1358.0

# the hypothesis refers to the amount of oil leaked into the water, which is also mentioned in the premise
# compute the total amount of oil leaked from the premise
total_leaked_oil_premise = total_oil_premise - leaked_oil_hypothesis
if total_leaked_oil_premise!= 0:
    # check if the amount of oil leaked from the hypothesis contradicts the amount of oil leaked from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
