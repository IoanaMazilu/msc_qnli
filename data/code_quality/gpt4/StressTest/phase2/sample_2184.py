years_premise = 4
years_hypothesis = 3

# the hypothesis talks about the time when John will be twice as old as Frank, also mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis value contradicts the premise's exact time
    label = "contradiction"
else:
    # the premise gives an exact time when John will be twice as old as Frank
    # any time less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
