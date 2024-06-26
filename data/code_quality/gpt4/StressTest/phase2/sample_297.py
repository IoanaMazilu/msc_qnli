years_premise = 5
years_hypothesis = 1

# the hypothesis talks about the time period when John will be twice as old as Frank, which is also mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis value contradicts the estimate of 'years_premise'
    label = "contradiction"
else:
    # any time period less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
