total_oil_premise = 6522.0
leaked_oil_premise = 5165.0
leaked_oil_hypothesis = 1357.0

# the hypothesis talks about the amount of oil leaked, which is also mentioned in the premise
# compute the actual amount of oil leaked in the premise
actual_leaked_oil_premise = total_oil_premise - leaked_oil_premise

if leaked_oil_hypothesis != actual_leaked_oil_premise:
    # check if the amount of oil leaked in the hypothesis contradicts the actual amount of oil leaked in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
