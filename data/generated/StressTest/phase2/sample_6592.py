# Premise: At the same time Joyce gets on an elevator on the more than 51 st floor of the same building and rides down at a rate of 93 floors per minute.
# Hypothesis: At the same time Joyce gets on an elevator on the 71 st floor of the same building and rides down at a rate of 93 floors per minute.
# Golden Label: neutral

floor_premise = 51
floor_hypothesis = 71
rate_premise = 93
rate_hypothesis = 93

# the hypothesis gives a specific floor number and the rate of ride down, both referenced in the premise
if floor_hypothesis <= floor_premise:
    # check if 'floor_hypothesis' contradicts the premise's estimate of more than 'floor_premise' 
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of ride down in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor number
    # any floor number greater than 'floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

