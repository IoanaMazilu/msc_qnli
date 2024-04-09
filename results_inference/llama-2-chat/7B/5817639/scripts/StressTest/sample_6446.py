years_premise = 14
years_hypothesis = 54

# the hypothesis talks about the age difference between two people, referenced also in the premise
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the estimate of 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
