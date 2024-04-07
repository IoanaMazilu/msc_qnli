# Premise: Lionel left his house and walked towards Walt's house, more than 28 miles away.
# Hypothesis: Lionel left his house and walked towards Walt's house, 48 miles away.
# Golden Label: neutral

distance_premise = 28
distance_hypothesis = 48

# the hypothesis talks about the distance Lionel walked, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

