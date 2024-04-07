# Premise: Steve gets on the elevator at the 11 th floor of a building and rides up at a rate of 57 floors per minute.
# Hypothesis: Steve gets on the elevator at the less than 11 th floor of a building and rides up at a rate of 57 floors per minute.
# Golden Label: contradiction

floor_premise = 11
floor_hypothesis = 11
rate_premise = 57
rate_hypothesis = 57

# the hypothesis refers to the floor number where Steve gets on the elevator and the speed of the elevator, both mentioned in the premise
if floor_hypothesis >= floor_premise:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the speed of the elevator in the hypothesis contradicts the speed of the elevator in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

