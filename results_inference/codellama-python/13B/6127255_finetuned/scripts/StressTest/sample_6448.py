years_premise = 8
years_hypothesis = 5

# the hypothesis talks about the number of years until John is twice as old as Frank, which is also referenced in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
