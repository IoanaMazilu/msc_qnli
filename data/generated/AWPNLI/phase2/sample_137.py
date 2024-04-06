# Premise: There are 4.0 squirrels in a tree with 2.0 nuts.
# Hypothesis: There are 5.0 more squirrels than nuts.
# Golden Label: contradiction

squirrels_premise = 4.0
nuts_premise = 2.0
squirrels_hypothesis = 5.0

# the hypothesis refers to the number of squirrels and nuts, which are also mentioned in the premise
# compute the difference between the number of squirrels and nuts in the premise
difference_premise = squirrels_premise - nuts_premise
if squirrels_hypothesis != difference_premise:
    # check if the difference in the hypothesis contradicts the difference from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

