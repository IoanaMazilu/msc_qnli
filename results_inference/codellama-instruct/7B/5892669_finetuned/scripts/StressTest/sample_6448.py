years_premise = 8
years_hypothesis = 5

# the hypothesis refers to the time when John will be twice as old as Frank, also mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis time contradicts the premise's estimate of less than 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
