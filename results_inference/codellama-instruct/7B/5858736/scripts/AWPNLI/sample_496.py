bananas_premise = 46.0
bananas_hypothesis = 51.0

# the hypothesis refers to the number of bananas in the jar, which are also mentioned in the premise
# compute the total number of bananas in the premise
total_bananas_premise = bananas_premise + 5.0
if total_bananas_hypothesis!= total_bananas_premise:
    # check if the number of bananas in the hypothesis contradicts the number of bananas from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
