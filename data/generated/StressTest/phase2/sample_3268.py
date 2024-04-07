# Premise: At the same time Joyce gets on an elevator on the more than 11 st floor of the same building and rides down at a rate of 63 floors per minute.
# Hypothesis: At the same time Joyce gets on an elevator on the 41 st floor of the same building and rides down at a rate of 63 floors per minute.
# Golden Label: neutral

floor_premise = 11
floor_hypothesis = 41
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about the floor Joyce is on and the rate of the elevator, both referenced also in the premise
if floor_hypothesis <= floor_premise:
    # check if the floor number in the hypothesis contradicts the estimate of more than 'floor_premise'
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor number
    # any floor number greater than 'floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

