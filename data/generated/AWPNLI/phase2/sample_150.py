# Premise: There are 12.0 birds on the fence and 8.0 more birds land on the fence.
# Hypothesis: 20.0 birds are on the fence.
# Golden Label: entailment

birds_on_fence_premise = 12.0
birds_landed_premise = 8.0
birds_total_hypothesis = 20.0

# the hypothesis refers to the total number of birds, which is also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_on_fence_premise + birds_landed_premise
if birds_total_hypothesis != total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

