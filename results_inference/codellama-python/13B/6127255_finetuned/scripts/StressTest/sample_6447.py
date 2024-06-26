years_premise = 5
years_hypothesis = 8

# the hypothesis refers to the same situation as the premise, but with a different time frame
if years_hypothesis < years_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # the premise gives a specific time frame when John will be twice as old as Frank
    # any time frame equal to or greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
