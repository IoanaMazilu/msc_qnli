# Premise: There are 12.0 birds on the fence and 8.0 more birds land on the fence.
# Hypothesis: 16.0 birds are on the fence.
# Golden Label: contradiction

birds_initially_premise = 12.0
landed_birds_premise = 8.0
birds_hypothesis = 16.0

# the hypothesis refers to the number of birds, which are also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_initially_premise + landed_birds_premise
if birds_hypothesis != total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

