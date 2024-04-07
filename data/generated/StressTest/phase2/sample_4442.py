# Premise: At the same time Joyce gets on an elevator on the 61 st floor of the same building and rides down at a rate of 78 floors per minute.
# Hypothesis: At the same time Joyce gets on an elevator on the less than 61 st floor of the same building and rides down at a rate of 78 floors per minute.
# Golden Label: contradiction

floor_premise = 61
floor_hypothesis = 61
rate_premise = 78
rate_hypothesis = 78

# the hypothesis refers to the same event mentioned in the premise
if floor_hypothesis > floor_premise:
    # check if the floor in hypothesis contradicts the floor in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in hypothesis contradicts the rate in premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

