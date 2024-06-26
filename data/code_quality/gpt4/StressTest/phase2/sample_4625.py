cleaning_time_premise = 6
cleaning_time_hypothesis = 6

# the hypothesis talks about the time John spends cleaning the house, mentioned also in the premise
if cleaning_time_hypothesis < cleaning_time_premise:
    # check if the hypothesis value contradicts the given 'cleaning_time_premise'
    label = "contradiction"
elif cleaning_time_hypothesis == cleaning_time_premise:
    # check if the hypothesis value matches exactly with the 'cleaning_time_premise'
    label = "entailment"
else:
    # the premise gives a specific time for John's cleaning
    # any time greater than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
