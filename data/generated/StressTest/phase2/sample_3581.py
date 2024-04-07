# Premise: John has 75 pencils, he distribute 20 pencils to his friends in his class.
# Hypothesis: John has 25 pencils, he distribute 20 pencils to his friends in his class.
# Golden Label: contradiction

pencils_premise = 75
pencils_distributed_premise = 20
pencils_hypothesis = 25
pencils_distributed_hypothesis = 20

# the hypothesis refers to the number of pencils John has and the number of pencils he distributed, both mentioned in the premise
if pencils_distributed_premise != pencils_distributed_hypothesis:
    # check if the number of pencils distributed in the hypothesis contradicts the number of pencils distributed in the premise
    label = "contradiction"
elif pencils_hypothesis != (pencils_premise - pencils_distributed_premise):
    # check if the number of pencils John has in the hypothesis contradicts the remaining pencils John has in the premise after distribution
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

