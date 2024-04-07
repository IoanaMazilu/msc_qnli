# Premise: Stalin gets on the elevator at the less than 31 th floor of a building and rides up at a rate of 57 floors per minute.
# Hypothesis: Stalin gets on the elevator at the 11 th floor of a building and rides up at a rate of 57 floors per minute.
# Golden Label: neutral

floor_premise = 31
floor_hypothesis = 11
rate_premise = 57
rate_hypothesis = 57

# The hypothesis refers to the floor Stalin gets on the elevator and the rate of riding up, both mentioned in the premise
if floor_hypothesis >= floor_premise:
    # check if the floor in the hypothesis contradicts the estimate of less than 'floor_premise' in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of riding up in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

