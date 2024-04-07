# Premise: At the same time Joyce gets on an elevator on the more than 11 st floor of the same building and rides down at a rate of 53 floors per minute.
# Hypothesis: At the same time Joyce gets on an elevator on the 51 st floor of the same building and rides down at a rate of 53 floors per minute.
# Golden Label: neutral

floor_premise = 11
floor_hypothesis = 51
rate_premise = 53
rate_hypothesis = 53

# the hypothesis talks about the floor number and rate of Joyce's elevator ride which were also mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis floor number contradicts the estimate of more than 'floor_premise'
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # the premise provides only an estimate for the floor number
    # any floor number greater than 'floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

