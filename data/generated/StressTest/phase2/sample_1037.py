# Premise: Lionel left his house and walked towards Walt's house, 48 miles away.
# Hypothesis: Lionel left his house and walked towards Walt's house, less than 48 miles away.
# Golden Label: contradiction

distance_to_walts_premise = 48
distance_to_walts_hypothesis = 48

# the hypothesis talks about the distance to Walt's house, also mentioned in the premise
if distance_to_walts_hypothesis >= distance_to_walts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_to_walts_premise'
    label = "contradiction"
else:
    # the premise gives an exact distance to Walt's house
    # any distance less than 'distance_to_walts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

