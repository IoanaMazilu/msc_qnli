marcella_shoes_premise = 27
marcella_shoes_hypothesis = float('inf')

# the hypothesis talks about the number of pairs of shoes Marcella has, referenced also in the premise
if marcella_shoes_hypothesis <= marcella_shoes_premise:
    # check if the hypothesis value contradicts the estimate of 27 pairs
    label = "contradiction"
elif marcella_shoes_hypothesis > marcella_shoes_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives a specific value for the number of pairs of shoes Marcella has
    # any number of pairs greater than 27 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
