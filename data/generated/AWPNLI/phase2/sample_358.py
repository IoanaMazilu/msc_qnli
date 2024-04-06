# Premise: There were 6.0 roses in the vase and Mary cut some roses from her flower garden and put 16.0 more roses in the vase.
# Hypothesis: 22.0 roses are now in the vase.
# Golden Label: entailment

roses_in_vase_premise = 6.0
added_roses_premise = 16.0
total_roses_hypothesis = 22.0

# the hypothesis refers to the total number of roses, which is also mentioned in the premise
# compute the total number of roses in the premise
total_roses_premise = roses_in_vase_premise + added_roses_premise
if total_roses_hypothesis != total_roses_premise:
    # check if the total number of roses in the hypothesis contradicts the total number of roses from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment" 

print(label)

