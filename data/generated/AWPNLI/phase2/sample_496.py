# Premise: Denise adds 5.0 bananas to a jar and there were originally 46.0 bananas in the jar.
# Hypothesis: 51.0 bananas are left in the jar.
# Golden Label: entailment

added_bananas_premise = 5.0
original_bananas_premise = 46.0
total_bananas_hypothesis = 51.0

# the hypothesis refers to the total number of bananas, which is related to the premise
# compute the total number of bananas in the premise
total_bananas_premise = added_bananas_premise + original_bananas_premise
if total_bananas_hypothesis != total_bananas_premise:
    # check if the number of bananas in the hypothesis contradicts the number of bananas from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

