# Premise: There were 6.0 roses in the vase and Mary cut some roses from her flower garden and put 16.0 more roses in the vase.
# Hypothesis: 18.0 roses are now in the vase.
# Golden Label: contradiction

roses_in_vase_premise = 6.0
added_roses_premise = 16.0
roses_in_vase_hypothesis = 18.0

# the hypothesis refers to the number of roses in the vase, which is also mentioned in the premise
# compute the total number of roses in the vase in the premise
total_roses_in_vase_premise = roses_in_vase_premise + added_roses_premise
if roses_in_vase_hypothesis != total_roses_in_vase_premise:
    # check if the number of roses in the vase in the hypothesis contradicts the number of roses in the vase from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

