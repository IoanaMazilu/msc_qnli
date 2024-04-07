# Premise: At the same time, Albert gets on an elevator at the 51 st floor of the same building and rides down at the rate of 63 floors per minute.
# Hypothesis: At the same time, Albert gets on an elevator at the less than 61 st floor of the same building and rides down at the rate of 63 floors per minute.
# Golden Label: entailment

floor_premise = 51
floor_hypothesis = 61
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the floor Albert started and the rate at which he's going down, both mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis estimate contradicts the floor number in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

