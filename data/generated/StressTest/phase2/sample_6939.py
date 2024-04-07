# Premise: At the same time Jose gets on an elevator on the 51 st floor of the same building and rides down at a rate of 63 floors per minute.
# Hypothesis: At the same time Jose gets on an elevator on the less than 61 st floor of the same building and rides down at a rate of 63 floors per minute.
# Golden Label: entailment

floor_premise = 51
floor_hypothesis = 61
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about the floor Jose starts at and the rate at which he rides down, both of which are mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the floor stated in the hypothesis contradicts the floor stated in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific floor and rate, any floor less than 'floor_hypothesis' and rate equal to 'rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

